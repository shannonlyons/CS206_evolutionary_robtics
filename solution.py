import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c

class SOLUTION:
    def __init__(self, myID):
        self.myID = myID
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1

    def Start_Simulation(self, directOrGui):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
       # os.system("python3 simulate.py " + directOrGui + " " + str(self.myID))
        os.system("python3 simulate.py " + directOrGui + " " + str(self.myID) + " 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        fitnessFile = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFile):
            time.sleep(0.01)

        f = open(fitnessFile, "r")
        self.fitness = float(f.read())
        f.close()
        os.remove(fitnessFile)

    def Create_World(self):
        worldFileName = "world" + str(self.myID) + ".sdf"
        pyrosim.Start_SDF(worldFileName)

        pyrosim.Send_Cube(name="Box", pos=[3, 3, 0.5], size=[1, 1, 1])

        pyrosim.End()

    def Create_Body(self):
        bodyFileName = "body" + str(self.myID) + ".urdf"
        pyrosim.Start_URDF(bodyFileName)

        # Torso
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1.5, 1, 1])

        # Upper legs
        pyrosim.Send_Joint(name="Torso_FrontLeg1", parent="Torso", child="FrontLeg1", type="revolute", position=[-0.2, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg1", pos=[-0.4, -0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_MiddleLeg1", parent="Torso", child="MiddleLeg1", type="revolute", position=[0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="MiddleLeg1", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_BackLeg1", parent="Torso", child="BackLeg1", type="revolute", position=[0.2, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg1", pos=[0.4, -0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_FrontLeg2", parent="Torso", child="FrontLeg2", type="revolute", position=[-0.2, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg2", pos=[-0.4, 0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_MiddleLeg2", parent="Torso", child="MiddleLeg2", type="revolute", position=[0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="MiddleLeg2", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_BackLeg2", parent="Torso", child="BackLeg2", type="revolute", position=[0.2, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg2", pos=[0.4, 0.5, 0], size=[0.2, 1, 0.2])


        # Lower legs
        pyrosim.Send_Joint(name="FrontLeg1_FrontLowerLeg1", parent="FrontLeg1", child="FrontLowerLeg1", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg1", pos=[-0.4, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="MiddleLeg1_MiddleLowerLeg1", parent="MiddleLeg1", child="MiddleLowerLeg1", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="MiddleLowerLeg1", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="BackLeg1_BackLowerLeg1", parent="BackLeg1", child="BackLowerLeg1", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg1", pos=[0.4, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="FrontLeg2_FrontLowerLeg2", parent="FrontLeg2", child="FrontLowerLeg2", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg2", pos=[-0.4, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="MiddleLeg2_MiddleLowerLeg2", parent="MiddleLeg2", child="MiddleLowerLeg2", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="MiddleLowerLeg2", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="BackLeg2_BackLowerLeg2", parent="BackLeg2", child="BackLowerLeg2", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg2", pos=[0.4, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()

    def Create_Brain(self):
        fileName = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(fileName)

        # pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        # pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        # pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        # pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="FrontLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="MiddleLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="BackLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="FrontLowerLeg2")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="MiddleLowerLeg2")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="BackLowerLeg2")

        # Motor neuron
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_FrontLeg1")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_MiddleLeg1")
        pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_BackLeg1")
        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_FrontLeg2")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_MiddleLeg2")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_BackLeg2")
        pyrosim.Send_Motor_Neuron(name=12, jointName="FrontLeg1_FrontLowerLeg1")
        pyrosim.Send_Motor_Neuron(name=13, jointName="MiddleLeg1_MiddleLowerLeg1")
        pyrosim.Send_Motor_Neuron(name=14, jointName="BackLeg1_BackLowerLeg1")
        pyrosim.Send_Motor_Neuron(name=15, jointName="FrontLeg2_FrontLowerLeg2")
        pyrosim.Send_Motor_Neuron(name=16, jointName="MiddleLeg2_MiddleLowerLeg2")
        pyrosim.Send_Motor_Neuron(name=17, jointName="BackLeg2_BackLowerLeg2")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])

        pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                             weight=self.weights[currentRow][currentColumn])
        pyrosim.End()


    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons -1)
        randomColumn = random.randint(0, c.numMotorNeurons -1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Set_ID(self):
        return self.myID