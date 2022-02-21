import numpy as np
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time

from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR
from constants import CONSTANTS

import robot as r

class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()
        # self.sensor = SENSOR()
        # self.motor = MOTOR()

        # Connect to pybullet, set additional search, set gravity, prep to simulate
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        pyrosim.Prepare_To_Simulate(r.robotId)

    def run(self):
        pass