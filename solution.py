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
      #  os.system("python3 simulate.py " + directOrGui + " " + str(self.myID))
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
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])

        # Upper legs
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[-0.1, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[-0.3, -0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_FrontLeg2", parent="Torso", child="FrontLeg2", type="revolute", position=[0.1, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg2", pos=[0.3, -0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[-0.1, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.3, 0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_BackLeg2", parent="Torso", child="BackLeg2", type="revolute", position=[0.1, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg2", pos=[0.3, 0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1.0, 0.2, 0.2])

        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1.0, 0.2, 0.2])


        # Lower legs
        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[-0.3, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="FrontLeg2_FrontLowerLeg2", parent="FrontLeg2", child="FrontLowerLeg2", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg2", pos=[0.3, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[-0.3, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="BackLeg2_BackLowerLeg2", parent="BackLeg2", child="BackLowerLeg2", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg2", pos=[0.3, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute", position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()

    def Create_Brain(self):
        fileName = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(fileName)

        # pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        # pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        # pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        # pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLowerLeg2")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="BackLowerLeg2")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="RightLowerLeg")

        # Motor neuron
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_FrontLeg2")
        pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_BackLeg2")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=13, jointName="FrontLeg2_FrontLowerLeg2")
        pyrosim.Send_Motor_Neuron(name=14, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=15, jointName="BackLeg2_BackLowerLeg2")
        pyrosim.Send_Motor_Neuron(name=16, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=17, jointName="RightLeg_RightLowerLeg")

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