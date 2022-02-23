import numpy as np
from constants import CONSTANTS
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):

        self.values = None

        self.motorValues = []
        self.jointName = jointName

        self.amplitude = -np.pi / 4
        self.frequency = 0.06
        self.offset = 0

        self.targetAngles = np.linspace(-np.pi, 2 * np.pi, 1000)

        MOTOR.Prepare_To_Act(self)

    def Prepare_To_Act(self):
        if (self.jointName == "Torso_FrontLeg"):
            for e in range(len(self.targetAngles)):
                self.motorValues.append(self.amplitude * np.sin((self.frequency * e) + self.offset))
        else:
            for e in range(len(self.targetAngles)):
                self.motorValues.append(self.amplitude * np.sin((self.frequency/2 * e) + self.offset))

    def Set_Value(self, i, robot):
        pyrosim.Set_Motor_For_Joint(robot, self.jointName, p.POSITION_CONTROL, self.motorValues[i], 20)

    def Save_Values(self):
        np.save("data/" + str(self.jointName) + "Joint", self.values)
