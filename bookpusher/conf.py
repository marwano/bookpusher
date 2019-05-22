from os.path import dirname, expanduser
import os

PORT = 8080
APP_SETTINGS = dict(
    debug=bool(os.environ.get('APP_DEBUG')),
    static_path=expanduser('~/bookpusher_images'),
    template_path=(dirname(__file__) + '/templates'),
)

BOOKS = list(range(1, 7))
DC = dict(
    speed=0.8,
    step_duration=0.38,
    forward=1,
    back=-1,
)
SERVO_MAX_ANGLE = 140
HAND = dict(
    up=SERVO_MAX_ANGLE,
    down=SERVO_MAX_ANGLE - 90,
    delay=0.7,
)
