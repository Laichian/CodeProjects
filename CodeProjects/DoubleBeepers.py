"""
File: DoubleBeepers.py
Name:Lydia Lai
-------------------------------
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    double_beeper()
    move_back()
    go_home()


def double_beeper():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()
        move()
        turn_around()


def move_back():
    move()
    # karel is on beeper
    while on_beeper():
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        turn_around()
        move()

def turn_around():
    turn_left()
    turn_left()


def go_home():
    turn_around()
    move()
    move()
    turn_around()















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)