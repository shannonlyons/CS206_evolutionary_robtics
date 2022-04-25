import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import time
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import math

import constants as c
import sensor as s

class ROBOT:
    def __init__(self, solutionID):

        self.solutionID = solutionID
        self.sensors = {}
        self.motors = {}

        bodyFileName = "body" + str(self.solutionID) + ".urdf"
        self.robotId = p.loadURDF(bodyFileName)

        fileName = "brain" + str(self.solutionID) + ".nndf"
        self.nn = NEURAL_NETWORK(fileName)


        pyrosim.Prepare_To_Simulate(self.robotId)

        ROBOT.Prepare_To_Sense(self)
        ROBOT.Prepare_To_Act(self)

        os.remove(bodyFileName)
        os.remove(fileName)

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    #
    def Sense(self, i):
        for s in self.sensors:
            self.sensors[s].Get_Value(i)

    def Think(self):
        self.nn.Update()

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = (self.nn.Get_Value_Of(neuronName)) * c.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle, self.robotId)

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        height = basePosition[2]

        fitnessFile = "fitness" + str(self.solutionID) + ".txt"
        tempFile = "tmp" + str(self.solutionID) + ".txt"
        f = open(tempFile, "w")
        os.system('mv ' + tempFile + ' ' + fitnessFile)
        f.write(str(xPosition))
      #  f.write(str(height))
        f.close()

        exit()