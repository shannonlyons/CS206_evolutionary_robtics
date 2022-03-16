import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import time
from pyrosim.neuralNetwork import NEURAL_NETWORK

import constants as c
import sensor as s

class ROBOT:
    def __init__(self):

        self.sensors = {}
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        ROBOT.Prepare_To_Sense(self)
        ROBOT.Prepare_To_Act(self)

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
          #  print(linkName)
            self.sensors[linkName] = SENSOR(linkName)
    #
    def Sense(self, i):
        for s in self.sensors:
            self.sensors[s].Get_Value(i)

    def Think(self):
        self.nn.Update()
       # self.nn.Print()

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            # print(linkName)
            self.motors[jointName] = MOTOR(jointName)

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(desiredAngle, self.robotId)
               # print('Neuron Name: ' + neuronName + ', Joint Name: ' + jointName + ', Desired Angle: ' + str(desiredAngle))

    def Get_Fitness(self):
        self.stateOfLinkZero = p.getLinkState(self.robotId,0)
        self.positionOfLinkZero = self.stateOfLinkZero[0]
        self.xCoordinateOfLinkZero = self.positionOfLinkZero[0]

        f = open("fitness.txt", "w")
        f.write(str(self.xCoordinateOfLinkZero))
        f.close()

        exit()