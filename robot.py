import pybullet as p
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self):
        self.sensor = SENSOR()
        self.motor = MOTOR()

        self.sensors
        self.motors

        self.robotId = p.loadURDF("body.urdf")