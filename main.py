import os
import cv2
import numpy as np
import time
import utils

from argparse import ArgumentParser
from collections import deque
from face_pose.pose_estimator import PoseEstimator
from face_pose.stabilizer import Stabilizer
from sock import Socket

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


def run():
    # Get operating system
    os = utils.get_os()

    if os == 'Windows':  # Windows OS
        cap = cv2.VideoCapture(args.cam + cv2.CAP_DSHOW)
    else:  # Linux & Mac OS
        cap = cv2.VideoCapture(args.cam)

    cap.set(cv2.CAP_PROP_FPS, 30)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    _, sample_frame = cap.read()

    # Setup face detection models
    if not args.gpu:  # CPU: use dlib
        import dlib
        dlib_model_path = 'face_pose/shape_predictor_68_face_landmarks.dat'
        shape_predictor = dlib.shape_predictor(dlib_model_path)
        face_detector = dlib.get_frontal_face_detector()

    else:  # GPU: use FAN (better)
        import face_alignment

        if os == 'Darwin':  # MacOS
            fa = face_alignment.FaceAlignment(
                face_alignment.LandmarksType._2D, device='mps')
        else:  # Windows, Linux
            fa = face_alignment.FaceAlignment(
                face_alignment.LandmarksType._2D, device='cuda')

        face_detector = fa.face_detector

    # Introduce pose estimator to solve pose, get one frame to setup the estimator according to the image size
    pose_estimator = PoseEstimator(img_size=sample_frame.shape[:2])

    # Introduce scalar stabilizers for pose
    pose_stabilizers = [Stabilizer(
        state_num=2,
        measure_num=1,
        cov_process=0.01,
        cov_measure=0.1) for _ in range(8)]

    # Establish a TCP connection to Unity
    if args.connect:
        address = ('127.0.0.1', args.port)
        sock = Socket()
        sock.connect(address)

    ts = []
    frame_count = 0
    no_face_count = 0
    prev_boxes = deque(maxlen=5)
    prev_marks = deque(maxlen=5)

    while True:
        # Get frames
        _, frame = cap.read()
        frame = cv2.flip(frame, 2)
        frame_count += 1

        # Send message data to Unity client
        if args.connect and frame_count > 60:
            sock.conv2msg()
            sock.send()

        t = time.time()

        # Loop
        # 1. Face detection, draw face and iris landmarks
        # 2. Pose estimation and stabilization (face + iris), calculate and calibrate data if error is low
        # 3. Data transmission with socket

        # Face detection on every odd frame
        if frame_count % 2 == 1:
            facebox = utils.get_face(face_detector, frame, args.gpu)
            if facebox is not None:
                no_face_count = 0
        else:
            if len(prev_boxes) > 1:  # use a linear movement assumption

                # Estimate no more than 1 frame
                if no_face_count > 1:
                    facebox = None
                else:
                    facebox = prev_boxes[-1] + \
                        np.mean(
                            np.diff(np.array(prev_boxes), axis=0), axis=0)[0]
                    facebox = facebox.astype(int)
                    no_face_count += 1

        # Face is detected
        if facebox is not None:
            prev_boxes.append(facebox)

            # Mark face and iris on each frame
            if not args.gpu:
                face = dlib.rectangle(left=facebox[0], top=facebox[1],
                                      right=facebox[2], bottom=facebox[3])
                marks = utils.shape_to_np(shape_predictor(frame, face))
            else:
                # Draw landmarks on first frame or each even frame
                if len(prev_marks) == 0 \
                        or frame_count == 1 \
                        or frame_count % 2 == 0:

                    face_img = frame[facebox[1]: facebox[3],
                                     facebox[0]: facebox[2]]
                    marks = fa.get_landmarks(face_img[:, :, ::-1],
                                             detected_faces=[(0, 0, facebox[2] - facebox[0], facebox[3] - facebox[1])])
                    marks = marks[-1]
                    marks[:, 0] += facebox[0]
                    marks[:, 1] += facebox[1]
                else:
                    if len(prev_marks) > 1:  # use a linear movement assumption
                        marks = prev_marks[-1] + \
                            np.mean(
                                np.diff(np.array(prev_marks), axis=0), axis=0)
                prev_marks.append(marks)

            x_l, y_l, ll, lu = utils.detect_iris(frame, marks, "left")
            x_r, y_r, rl, ru = utils.detect_iris(frame, marks, "right")

            # Pose estimation with 68 points
            error, R, T = pose_estimator.solve_pose_by_68_points(marks)
            pose = list(R) + list(T)

            # Stabilize iris position
            pose += [(ll + rl) / 2.0, (lu + ru) / 2.0]

            # Large error means tracking fails: reinitialize pose estimator
            if error > 100:
                # At the same time, keep sending the same information (e.g. same roll)
                pose_estimator = PoseEstimator(img_size=sample_frame.shape[:2])

            else:
                # Stabilize the pose
                steady_pose = []
                pose_np = np.array(pose, dtype=object).flatten()
                for value, ps_stb in zip(pose_np, pose_stabilizers):
                    ps_stb.update([value])
                    steady_pose.append(ps_stb.state[0])

                if args.connect:
                    # head
                    roll = np.clip(
                        -(180 + np.degrees(steady_pose[2])), -50, 50)
                    pitch = np.clip(
                        -(np.degrees(steady_pose[1])), -50, 50)
                    yaw = np.clip(-(np.degrees(steady_pose[0])), -50, 50)

                    # eyes
                    earLeft = utils.eye_aspect_ratio(marks[36:42])
                    earRight = utils.eye_aspect_ratio(marks[42:48])
                    eyeballX = steady_pose[6]
                    eyeballY = steady_pose[7]

                    # eyebrows
                    barLeft = utils.brow_aspect_ratio(marks[17:22])
                    barRight = utils.brow_aspect_ratio(marks[22:27])

                    # mouth
                    mouthWidthRatio = utils.mouth_distance(
                        marks[60:68]) / (facebox[2] - facebox[0])
                    mouthOpen = utils.mouth_aspect_ratio(marks[60:68])

                    # Calibration before data transmission
                    # eye openness
                    eyeOpenLeft = utils.calibrate_eyeOpen(
                        earLeft, sock.eyeOpenLeftLast, args.gpu)
                    eyeOpenRight = utils.calibrate_eyeOpen(
                        earRight, sock.eyeOpenRightLast, args.gpu)

                    # eyeballs
                    eyeballX, eyeballY = utils.calibrate_eyeball(
                        eyeballX, eyeballY)

                    # eyebrows
                    eyebrowLeft = utils.calibrate_eyebrow(
                        barLeft, sock.eyebrowLeftLast, args.gpu)
                    eyebrowRight = utils.calibrate_eyebrow(
                        barRight, sock.eyebrowRightLast, args.gpu)

                    # mouth width
                    mouthWidth = utils.calibrate_mouthWidth(
                        mouthWidthRatio, args.gpu)

                    # Update
                    sock.update_all(roll, pitch, yaw, eyeOpenLeft, eyeOpenRight, eyeballX,
                                    eyeballY, eyebrowLeft, eyebrowRight, mouthWidth, mouthOpen)

            # In debug mode, show the marks
            if args.debug:

                # Show facebox
                # utils.draw_box(frame, [facebox])

                # Show iris
                if x_l > 0 and y_l > 0:
                    utils.draw_iris(frame, x_l, y_l, color=(0, 255, 255))
                if x_r > 0 and y_r > 0:
                    utils.draw_iris(frame, x_r, y_r, color=(0, 255, 255))

                if error < 100:
                    # Show face landmarks
                    utils.draw_marks(
                        frame, marks, color=(255, 255, 0))  # cyan

                    # Show frame of stable pose
                    pose_estimator.draw_annotation_box(
                        frame, np.expand_dims(steady_pose[:3], 0), np.expand_dims(
                            steady_pose[3:6], 0),
                        color=(203, 192, 255))  # pink

                    # Draw head axes on frame
                    pose_estimator.draw_axes(frame, np.expand_dims(steady_pose[:3], 0),
                                             np.expand_dims(steady_pose[3:6], 0))

        dt = time.time() - t
        ts += [dt]
        FPS = int(1 / (np.mean(ts[-10:]) + 1e-6))
        print('\r', 'Time: %.3f' % dt, end=' ')

        if args.debug:
            utils.draw_FPS(frame, FPS)
            cv2.imshow("face", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to exit
                break

    # Close all if program is terminated
    cap.release()
    if args.connect:
        sock.close()
    if args.debug:
        cv2.destroyAllWindows()
    print('Time: %.3f' % np.mean(ts))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--cam", type=int,
                        help="specify the index of camera if there are multiple cameras",
                        default=0)
    parser.add_argument("--debug", action="store_true",
                        help="show image and marks",
                        default=False)
    parser.add_argument("--gpu", action="store_true",
                        help="use GPU to do face detection and face landmark detection",
                        default=False)
    parser.add_argument("--connect", action="store_true",
                        help="connect to unity character",
                        default=False)
    parser.add_argument("--port", type=int,
                        help="set port number to connect",
                        default=14514)
    args = parser.parse_args()

    run()
