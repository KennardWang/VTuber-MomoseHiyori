import os
import cv2
import numpy as np
import socket
import time
import dlib
import face_alignment
import utils

from platform import system
from argparse import ArgumentParser
from collections import deque
from face_pose.pose_estimator import PoseEstimator
from face_pose.stabilizer import Stabilizer

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


class Socket:
    """Socket class for message transmission"""

    def __init__(self):
        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0
        self.eye_open = 0.0
        self.eye_diff = 0.0
        self.eyeballX = 0.0
        self.eyeballY = 0.0
        self.mouthWidth = 0.0
        self.mouthVar = 0.0

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def update_all(self, roll, pitch, yaw, eye_open, eye_diff, eyeballX, eyeballY, mouthWidth, mouthVar):
        """Update all variables"""
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
        self.eye_open = eye_open
        self.eye_diff = eye_diff
        self.eyeballX = eyeballX
        self.eyeballY = eyeballY
        self.mouthWidth = mouthWidth
        self.mouthVar = mouthVar

    def conv2msg(self):
        """Convert all variables to message data"""
        self.msg = '%.4f %.4f %.4f %.4f %.4f %.4f %.4f %.4f %.4f' % \
            (self.roll, self.pitch, self.yaw, self.eye_open, self.eye_diff,
             self.eyeballX, self.eyeballY, self.mouthWidth, self.mouthVar)

    def connect(self, addr):
        """Establish connection"""
        self.s.connect(addr)

    def send(self):
        """Sending message data"""
        self.s.send(bytes(self.msg, "utf-8"))

    def close(self):
        """Close socket"""
        self.s.close()


def def_os():
    if system() in ['Windows']:  # Windows OS
        cap = cv2.VideoCapture(args.cam + cv2.CAP_DSHOW)
    else:  # Linux & Mac OS
        cap = cv2.VideoCapture(args.cam)
    return cap


def get_face(detector, image, gpu=False):
    if not gpu:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        try:
            box = detector(image)[0]
            x1 = box.left()
            y1 = box.top()
            x2 = box.right()
            y2 = box.bottom()
            return [x1, y1, x2, y2]
        except Exception:
            return None
    else:
        image = cv2.resize(image, None, fx=0.5, fy=0.5)
        box = detector.detect_from_image(image)[0]
        if box is None:
            return None
        return (2 * box[:4]).astype(int)


def run():
    # Define operating system
    cap = def_os()
    cap.set(cv2.CAP_PROP_FPS, 30)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    _, sample_frame = cap.read()

    # Setup face detection models
    if not args.gpu:  # CPU: use dlib
        dlib_model_path = 'face_pose/shape_predictor_68_face_landmarks.dat'
        shape_predictor = dlib.shape_predictor(dlib_model_path)
        face_detector = dlib.get_frontal_face_detector()
    else:  # GPU: use FAN (better)
        fa = face_alignment.FaceAlignment(
            face_alignment.LandmarksType._2D, flip_input=False)
        face_detector = fa.face_detector

    # Introduce pose estimator to solve pose, get one frame to setup the estimator according to the image size
    pose_estimator = PoseEstimator(img_size=sample_frame.shape[:2])

    # Introduce scalar stabilizers for pose
    pose_stabilizers = [Stabilizer(
        state_num=2,
        measure_num=1,
        cov_process=0.01,
        cov_measure=0.1) for _ in range(8)]

    # Establish a TCP connection to unity.
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
        # 1. Face detection
        # 2. Draw face and iris landmarks
        # 3. Pose estimation and stabilization (face + iris)
        # 4. Calculate and calibrate message data if low error
        # 5. Data transmission with socket

        # Face detection on every odd frame
        if frame_count % 2 == 1:
            facebox = get_face(face_detector, frame, args.gpu)
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

            # Mark face and iris on every frame
            if not args.gpu:
                face = dlib.rectangle(left=facebox[0], top=facebox[1],
                                      right=facebox[2], bottom=facebox[3])
                marks = utils.shape_to_np(shape_predictor(frame, face))
            else:
                # Draw landmarks on first frame or every even frame
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
                    # Calibrate: pitch(15 is camera angle), eyeballX, eyeballY, mouthWidth
                    # Head
                    roll = np.clip(
                        -(180 + np.degrees(steady_pose[2])), -50, 50)
                    pitch = np.clip(
                        -(np.degrees(steady_pose[1]) + 15), -40, 40)
                    yaw = np.clip(-(np.degrees(steady_pose[0])), -50, 50)

                    # Eyes
                    eye_left = utils.eye_aspect_ratio(marks[36:42])
                    eye_right = utils.eye_aspect_ratio(marks[42:48])
                    eye_open = (eye_left + eye_right) / 2
                    eye_diff = abs(eye_left - eye_right)
                    eyeballX = (steady_pose[6] - 0.45) * (-4)
                    eyeballY = (steady_pose[7] - 0.38) * 2

                    # Mouth
                    mouthWidth = utils.mouth_distance(
                        marks[60:68]) / (facebox[2] - facebox[0]) + 0.4
                    mouthVar = utils.mouth_aspect_ration(marks[60:68])

                    # Update
                    sock.update_all(roll, pitch, yaw, eye_open, eye_diff,
                                    eyeballX, eyeballY, mouthWidth, mouthVar)

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
            if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to exit.
                break

    # Close all if terminated
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
