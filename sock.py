import socket


class Socket:
    """Socket class for message transmission"""

    def __init__(self):
        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0
        self.eyeLeft = 0.0
        self.eyeRight = 0.0
        self.eyeDiff = 0.0
        self.diffThres = 0.0  # diff threshold
        self.eyeballX = 0.0
        self.eyeballY = 0.0
        self.mouthWidth = 0.0
        self.mouthVar = 0.0

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def update_all(self, roll, pitch, yaw, eyeLeft, eyeRight, eyeDiff, diffThres, eyeballX, eyeballY, mouthWidth, mouthVar):
        """Update all variables"""
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
        self.eyeLeft = eyeLeft
        self.eyeRight = eyeRight
        self.eyeDiff = eyeDiff
        self.diffThres = diffThres
        self.eyeballX = eyeballX
        self.eyeballY = eyeballY
        self.mouthWidth = mouthWidth
        self.mouthVar = mouthVar

    def conv2msg(self):
        """Convert all variables to message data"""
        self.msg = '%.4f %.4f %.4f %.4f %.4f %.4f %.4f %.4f %.4f %.4f %.4f' % \
            (self.roll, self.pitch, self.yaw, self.eyeLeft, self.eyeRight, self.eyeDiff, self.diffThres,
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
