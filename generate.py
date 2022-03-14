import pyrosim.pyrosim as pyrosim

# size variables
length = 1
width = 1
height = 1

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[length,width,height])
    pyrosim.Send_Joint(name = "Torso_FrontLeg", parent= "Torso", child = "FrontLeg", type = "revolute", position = [2,0,1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1,0,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[length, width, height])

    pyrosim.End()


def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")

    # Sensor neuron
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

    # Motor neuron
    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

    # Synapse
    pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=-1.5)
    pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=-1.5)
    pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=-0.2)

    pyrosim.End()

Generate_Body()
Generate_Brain()