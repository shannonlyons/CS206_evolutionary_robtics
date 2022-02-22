import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR

import constants as c
import sensor as s

class ROBOT:
    def __init__(self):
        self.sensor = SENSOR()
        self.motor = MOTOR()
    #    self.Prepare_To_Sense()


    #
      #  self.robotId = p.loadURDF("body.urdf")
    #
    def Prepare_To_Sense(self):
        self.sensors = {}
        self.motors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    #
    # def Sense(self, sensors):
    #     for i in self.sensors:
    #         s.Get_Value()