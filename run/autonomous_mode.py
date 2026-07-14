#!/usr/bin/env python3

from robot import Robot
from ddd


# Autonomous run

if __name__ == '__main__':
    bot = Robot()
    behavior = AutonomousBehavior(bot)
    behavior.run(20)
    behavior.test_sensor()
