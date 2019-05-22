from os.path import dirname
import os

PORT = 8080
APP_SETTINGS = dict(
    debug=bool(os.environ.get('APP_DEBUG')),
    static_path=(dirname(__file__) + '/static'),
    template_path=(dirname(__file__) + '/templates'),
)

SERVO_MAX_ANGLE = 140
DC_SPEED = 1.0
TURN_DURATION = 0.2
DIRECTION = dict(
    forward=[1, 1],
    right=[1, 0],
    left=[0, 1],
    back=[-1, -1],
    stop=[0, 0],
)

ANGLES = {}
ANGLES['raise'] = SERVO_MAX_ANGLE
ANGLES['lower'] = SERVO_MAX_ANGLE - 90
