from adafruit_crickit import crickit
import time
import random
from .conf import BOOKS, DC, SERVO_MAX_ANGLE, HAND


def move_dc(direction, steps):
    crickit.dc_motor_1.throttle = direction * DC['speed']
    crickit.dc_motor_2.throttle = direction * DC['speed']
    time.sleep(DC['step_duration'] * steps)
    crickit.dc_motor_1.throttle = 0
    crickit.dc_motor_2.throttle = 0


def swipe_hand():
    crickit.servo_1.angle = HAND['down']
    time.sleep(HAND['delay'])
    crickit.servo_1.angle = HAND['up']
    time.sleep(HAND['delay'])


def push_book(position):
    if position > 1:
        move_dc(DC['forward'], position - 1)
    swipe_hand()
    move_dc(DC['back'], position)


def push_all():
    books = list(BOOKS)
    random.shuffle(books)
    for book in books:
        push_book(book)


def init_servo():
    crickit.servo_1.actuation_range = SERVO_MAX_ANGLE
