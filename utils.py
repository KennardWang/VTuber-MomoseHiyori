import numpy as np
from platform import system
import cv2


def get_os():
    """Get operating system"""
    return system()


def get_face(detector, image, gpu=False):
    """Capture face"""
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


def eye_aspect_ratio(eye):
    """eye: np.array, shape (6, 2)"""
    ear = np.linalg.norm(eye[1] - eye[5]) + np.linalg.norm(eye[2] - eye[4])
    ear /= (2 * np.linalg.norm(eye[0] - eye[3]) + 1e-6)
    return ear


def brow_aspect_ratio(brow):
    """brow: np.array, shape (5, 2)"""
    mid_point = (brow[0] + brow[4]) / 2
    bar = np.linalg.norm(brow[2] - mid_point) / \
        (np.linalg.norm(brow[0] - brow[4]) + 1e-6)
    return bar


def mouth_aspect_ratio(mouth):
    """mouth: np.array, shape (8, 2)"""
    mar = np.linalg.norm(mouth[1] - mouth[7]) + np.linalg.norm(
        mouth[2] - mouth[6]) + np.linalg.norm(mouth[3] - mouth[5])
    mar /= (2 * np.linalg.norm(mouth[0] - mouth[4]) + 1e-6)
    return mar


def mouth_distance(mouth):
    """Calculate mouth distance"""
    return np.linalg.norm(mouth[0] - mouth[4])


def detect_iris(frame, marks, side='left'):
    """
    Returns
    -------
    x: x coordinate of iris
    y: y coordinate of iris
    x_rate: how much iris is toward the left, 0 = totally left, 1 = totally right
    y_rate: how much iris is toward the top, 0 = totally top, 1 = totally bottom

    """

    mask = np.full(frame.shape[:2], 255, np.uint8)
    if side == 'left':
        region = marks[36:42].astype(np.int32)
    elif side == 'right':
        region = marks[42:48].astype(np.int32)
    try:
        cv2.fillPoly(mask, [region], (0, 0, 0))
        eye = cv2.bitwise_not(frame, frame.copy(), mask=mask)

        # Cropping on the eye
        margin = 4
        min_x = np.min(region[:, 0]) - margin
        max_x = np.max(region[:, 0]) + margin
        min_y = np.min(region[:, 1]) - margin
        max_y = np.max(region[:, 1]) + margin

        eye = eye[min_y:max_y, min_x:max_x]
        eye = cv2.cvtColor(eye, cv2.COLOR_RGB2GRAY)

        eye_binarized = cv2.threshold(eye, np.quantile(
            eye, 0.2), 255, cv2.THRESH_BINARY)[1]
        contours, _ = cv2.findContours(
            eye_binarized, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        contours = sorted(contours, key=cv2.contourArea)
        moments = cv2.moments(contours[-2])

        x = int(moments['m10'] / moments['m00']) + min_x
        y = int(moments['m01'] / moments['m00']) + min_y
        x_rate = (x - min_x - margin) / (max_x - min_x - 2 * margin)
        y_rate = (y - min_y - margin) / (max_y - min_y - 2 * margin)

        return x, y, x_rate, y_rate

    except Exception:
        return 0, 0, 0.5, 0.5


def shape_to_np(shape):
    """Convert shape to numpy"""
    coords = np.zeros((68, 2))
    for i in range(68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords


def draw_box(image, boxes, box_color=(255, 255, 255)):
    """Draw square boxes on image, color=(b, g, r)"""
    for box in boxes:
        cv2.rectangle(image,
                      (box[0], box[1]),
                      (box[2], box[3]), box_color, 3)


def draw_marks(image, marks, color=(255, 255, 255)):
    """Draw mark points on image, color=(b, g, r)"""
    for mark in marks:
        cv2.circle(image, (int(mark[0]), int(
            mark[1])), 1, color, -1, cv2.LINE_AA)


def draw_iris(frame, x, y, color=(255, 255, 255)):
    """Draw iris position, color=(b, g, r)"""
    cv2.line(frame, (x - 5, y), (x + 5, y), color)
    cv2.line(frame, (x, y - 5), (x, y + 5), color)


def draw_FPS(frame, FPS):
    """Draw FPS"""
    cv2.putText(frame, "FPS: %d" % FPS, (40, 40),
                cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 1)


def calibrate_eyeOpen(ear, eyeOpenLast, gpu):
    """Calibrate parameter eyeOpen"""
    flag = False  # jump out current state

    if not gpu:
        # CPU env
        if eyeOpenLast == 0.0:
            if ear > 0.17:
                flag = True
        if eyeOpenLast == 0.5:
            if abs(ear - 0.15) > 0.03:
                flag = True
        elif eyeOpenLast == 1.0:
            if abs(ear - 0.19) > 0.035:
                flag = True
        else:
            if ear < 0.22:
                flag = True

        if flag:
            if ear <= 0.14:
                eyeOpen = 0.0
            elif ear > 0.14 and ear <= 0.16:
                eyeOpen = 0.5
            elif ear > 0.16 and ear <= 0.22:
                eyeOpen = 1.0
            else:
                eyeOpen = 1.2
        else:
            eyeOpen = eyeOpenLast

    else:
        # GPU env
        if eyeOpenLast == 0.0:
            if ear > 0.25:
                flag = True
        if eyeOpenLast == 0.5:
            if abs(ear - 0.21) > 0.04:
                flag = True
        elif eyeOpenLast == 1.0:
            if abs(ear - 0.24) > 0.07:
                flag = True
        else:
            if ear < 0.17:
                flag = True

        if flag:
            if ear <= 0.22:
                eyeOpen = 0.0
            elif ear > 0.22 and ear <= 0.23:
                eyeOpen = 0.5
            elif ear > 0.23 and ear <= 0.27:
                eyeOpen = 1.0
            else:
                eyeOpen = 1.2
        else:
            eyeOpen = eyeOpenLast

    return eyeOpen


def calibrate_eyeball(eyeballX, eyeballY):
    """Calibrate parameters eyeballX, eyeballY"""
    return (eyeballX - 0.45) * (-4.0), (eyeballY - 0.38) * 2.0


def calibrate_eyebrow(bar, eyebroLast, gpu):
    """Calibrate parameter eyebrow"""
    flag = False  # jump out current state

    if not gpu:
        # CPU env
        if eyebroLast == -1.0:
            if bar > 0.22:
                flag = True
        else:
            if bar < 0.2:
                flag = True

        if flag:
            if bar <= 0.215:
                eyebrow = -1.0
            else:
                eyebrow = 0.0
        else:
            eyebrow = eyebroLast
    else:
        # GPU env
        if eyebroLast == -1.0:
            if bar > 0.22:
                flag = True
        else:
            if bar < 0.2:
                flag = True

        if flag:
            if bar <= 0.225:
                eyebrow = -1.0
            else:
                eyebrow = 0.0
        else:
            eyebrow = eyebroLast

    return eyebrow


def calibrate_mouthWidth(mouthWidthRatio, gpu):
    """Calibrate parameter mouthWidth"""
    if not gpu:
        # CPU env
        if mouthWidthRatio <= 0.27:
            mouthWidth = -0.5
        elif mouthWidthRatio > 0.27 and mouthWidthRatio <= 0.35:
            mouthWidth = 18.75 * mouthWidthRatio - 5.5625
        else:
            mouthWidth = 1.0
    else:
        # GPU env
        if mouthWidthRatio <= 0.32:
            mouthWidth = -0.5
        elif mouthWidthRatio > 0.32 and mouthWidthRatio <= 0.37:
            mouthWidth = 30.0 * mouthWidthRatio - 10.1
        else:
            mouthWidth = 1.0

    return mouthWidth
