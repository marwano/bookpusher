from adafruit_crickit import crickit
import time
from .conf import SERVO_MAX_ANGLE, DC_SPEED, TURN_DURATION, DIRECTION, ANGLES


def move_servo(action):
    crickit.servo_1.angle = ANGLES[action]


def move_dc(action):
    direction = DIRECTION[action]
    crickit.dc_motor_1.throttle = direction[0] * DC_SPEED
    crickit.dc_motor_2.throttle = direction[1] * DC_SPEED
    if action in ['right', 'left']:
        time.sleep(TURN_DURATION)
        crickit.dc_motor_1.throttle = 0
        crickit.dc_motor_2.throttle = 0


def move(action):
    if action in ['raise', 'lower']:
        move_servo(action)
    else:
        move_dc(action)


def init_servo():
    crickit.servo_1.actuation_range = SERVO_MAX_ANGLE
