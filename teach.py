from adafruit_crickit import crickit

SG5010_ACTUATION_RANGE = 140


class Robot:
    def __init__(self):
        crickit.servo_1.actuation_range = SG5010_ACTUATION_RANGE

    @property
    def wheel(self):
        return crickit.dc_motor_1.throttle

    @wheel.setter
    def wheel(self, throttle):
        crickit.dc_motor_1.throttle = throttle

    @property
    def arm(self):
        return crickit.servo_1.angle

    @arm.setter
    def arm(self, angle):
        crickit.servo_1.angle = angle

    @property
    def touch(self):
        return crickit.touch_1.value


r = Robot()
