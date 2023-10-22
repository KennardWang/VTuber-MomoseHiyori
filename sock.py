import socket


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
