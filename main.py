#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import Feladatok
import kulsoA2
import belsoA2
import kozepsoA2

oraiMunka=kozepsoA2.Palya()

oraiMunka.palya2()
oraiMunka.koszon()



# Create your objects here.
#ev3 = EV3Brick()

# főprogram
#elöző órai munkák megoldása
# oraiMunka.elsoFeladat()
# oraiMunka.masodikFeladat()
# oraiMunka.harmadikFeladat()
# oraiMunka.negyedikFeladat()
# fordulások
#oraiMunka.korbefordul2()
#oraiMunka.korbefordul3()
# Hangkezelés, téglavilágítás
# oraiMunka.koszon()


# Write your program here.
#ev3.speaker.beep()
#oraiMunka.csipog()