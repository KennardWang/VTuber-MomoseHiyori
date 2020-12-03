"""
Miscellaneous functions implemented by me.
"""

import numpy as np
import cv2
import math

def eye_aspect_ratio(eye):
    """
    eye: array of shape 6x2
    """
    ear = np.linalg.norm(eye[1]-eye[5]) + np.linalg.norm(eye[2]-eye[4])
    ear/= (2*np.linalg.norm(eye[0]-eye[3])+1e-6)
    return ear

def mouth_aspect_ration(mouth):
    mar = np.linalg.norm(mouth[1]-mouth[7]) + np.linalg.norm(mouth[2]-mouth[6]) + np.linalg.norm(mouth[3]-mouth[5])
    mar/= (2*np.linalg.norm(mouth[0]-mouth[4])+1e-6)
    return mar

def mouth_distance(mouth):
    return np.linalg.norm(mouth[0]-mouth[4])

def eyebrow_distance(eye, brow):
    """
    eye: array of shape 6:2
    brow: array of shape 5:2
    """
    eyeCenter = np.mean(eye, axis=0)
    browCenter = np.mean(brow, axis=0)
    browDistance = np.linalg.norm(brow[0] - brow[4])
    return np.linalg.norm(eyeCenter - browCenter) / browDistance

def detect_iris(frame, marks):
    """
    return:
       x: the x coordinate of the iris.
       y: the y coordinate of the iris.
       x_rate: how much the iris is toward the left. 0 means totally left and 1 is totally right.
       y_rate: how much the iris is toward the top. 0 means totally top and 1 is totally bottom.
    """
    mask = np.full(frame.shape[:2], 255, np.uint8)
    region = marks.astype(np.int32)

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

        eye_binarized = cv2.threshold(eye, np.quantile(eye, 0.2), 255, cv2.THRESH_BINARY)[1]
        contours, _ = cv2.findContours(eye_binarized, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # the first contour is the whole image, so we ignore that
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[1:]
        moments = cv2.moments(contours[0])
        # position of the center of the eye in the cropped image (centroid of contour)
        x = int(moments['m10'] / moments['m00'])
        y = int(moments['m01'] / moments['m00'])
        # fractional position of the center of the eye between 0 and 1
        normalizedx = x / (max_x - min_x)
        normalizedy = y / (max_y - min_y)


        # these are rotation invariant measures of roundness from the contour, but they don't seem to work as well as the ratio
        # calculate the roundness
        #eccentricity = ((moments['m20'] - moments['m02']) ** 2 - 4 * (moments['m11'] ** 2)) / ((moments['m20'] + moments['m02']) ** 2)
        # calculate the roundness
        #roundness = cv2.arcLength(contours[0], True) ** 2 / cv2.contourArea(contours[0]) - 2 * math.pi

        # calculate the openness of the eye based on the ratio of the contour
        rect = cv2.minAreaRect(contours[0])
        _, (width, height), _ = rect
        contour_ratio = min(width, height) / max(width, height)

        return x + min_x, y + min_y, normalizedx, normalizedy, contour_ratio, contours + [np.int0(cv2.boxPoints(rect))], min_x, min_y
    except:
        return 0, 0, 0.5, 0.5, 0.5, [], None, None

def shape_to_np(shape):
    coords = np.zeros((68, 2))
    for i in range(68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords