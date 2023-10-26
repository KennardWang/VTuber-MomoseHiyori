import socket


class Socket:
    """Socket class for message data transmission"""

    def __init__(self):
        self.roll = 0.0  # rotate along inner axis
        self.pitch = 0.0  # rotate along horizontal axis
        self.yaw = 0.0  # rotate along vertical axis
        self.eyeOpenLeft = 0.0  # degree of left eye openness
        self.eyeOpenRight = 0.0  # degree of right eye openness
        self.eyeballX = 0.0  # horizontal position of two eyes (has same ratio)
        self.eyeballY = 0.0  # vertical position of two eyes (has same ratio)
        self.eyebrowLeft = 0.0  # vertical position of left eyebrow
        self.eyebrowRight = 0.0  # vertical position of right eyebrow
        self.mouthWidth = 0.0  # mouth width / face width
        self.mouthOpen = 0.0  # degree of mouth openness

        self.eyeOpenLeftLast = self.eyeOpenLeft  # last frame
        self.eyeOpenRightLast = self.eyeOpenRight  # last frame
        self.eyebrowLeftLast = self.eyebrowLeft  # last frame
        self.eyebrowRightLast = self.eyebrowRight  # last frame

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def update_all(self, roll, pitch, yaw, eyeOpenLeft, eyeOpenRight, eyeballX, eyeballY, eyebrowLeft, eyebrowRight, mouthWidth, mouthOpen):
        """Update all parameters"""
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
        self.eyeOpenLeft = eyeOpenLeft
        self.eyeOpenRight = eyeOpenRight
        self.eyeballX = eyeballX
        self.eyeballY = eyeballY
        self.eyebrowLeft = eyebrowLeft
        self.eyebrowRight = eyebrowRight
        self.mouthWidth = mouthWidth
        self.mouthOpen = mouthOpen

        # Update some values of last frames
        self.eyeOpenLeftLast = self.eyeOpenLeft
        self.eyeOpenRightLast = self.eyeOpenRight
        self.eyebrowLeftLast = self.eyebrowLeft
        self.eyebrowRightLast = self.eyebrowRight

    def conv2msg(self):
        """Convert all parameters to message data"""
        self.msg = '%.4f %.4f %.4f %.4f %.4f %.4f %.4f %.4f %.4f %.4f %.4f' % \
            (self.roll, self.pitch, self.yaw, self.eyeOpenLeft, self.eyeOpenRight,
             self.eyeballX, self.eyeballY, self.eyebrowLeft, self.eyebrowRight, self.mouthWidth, self.mouthOpen)

    def connect(self, addr):
        """Establish connection"""
        self.s.connect(addr)

    def send(self):
        """Sending message data"""
        self.s.send(bytes(self.msg, "utf-8"))

    def close(self):
        """Close socket"""
        self.s.close()
