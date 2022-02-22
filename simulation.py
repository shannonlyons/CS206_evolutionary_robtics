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
import world as w
import sensor as s
import constants as c

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.world = WORLD()
        self.robot = ROBOT()

        p.setGravity(0,0,-9.8)
        pyrosim.Prepare_To_Simulate(p.loadURDF("body.urdf"))
       # r.Prepare_To_Sense()
      #  p.disconnect()

    def Run(self):

        for i in range(1000):
            print(i)
            p.stepSimulation()
            # r.Sense()
            # pyrosim.Set_Motor_For_Joint(r.robotId, "Torso_BackLeg", p.POSITION_CONTROL, self.back_sin_array[i], 20)
            # pyrosim.Set_Motor_For_Joint(r.robotId, "Torso_FrontLeg", p.POSITION_CONTROL, self.front_sin_array[i], 20)
            time.sleep(1/120)

        #p.disconnect()
        # self.back_sin_array = []
        # self.front_sin_array = []
        #
        # for e in range(len(c.targetAngles)):
        #     self.back_sin_array.append(c.back_amplitude * np.sin((c.back_frequency * e) + c.back_phaseOffset))
        #
        # for e in range(len(c.targetAngles)):
        #     self.front_sin_array.append(c.front_amplitude * np.sin((c.front_frequency * e) + c.front_phaseOffset))
        #
        #     # sin_array = []
        #     # for e in targetAngles:
        #     #     sin_array.append(np.sin(e))
        #
        # np.save('data/targetAngles.npy', self.back_sin_array)
        # np.save('data/targetAngles.npy', self.front_sin_array)


    def __del__(self):
        p.disconnect()