import pybullet as p
import numpy as np
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

p.loadSDF("world.sdf")
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

amplitude = np.pi/4
frequency = 1
phaseOffset = 0

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

# Left off at step 38
targetAngles = np.linspace(-np.pi/4, np.pi/4, 1000)
# np.save('data/targetAngles.npy', targetAngles)

for i in range (1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(robotId, "Torso_BackLeg", p.POSITION_CONTROL, targetAngles[i], 20)
    pyrosim.Set_Motor_For_Joint(robotId, "Torso_FrontLeg", p.POSITION_CONTROL, targetAngles[i], 20)
    time.sleep(1/240)

# save here
np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)

print('Back leg:')
print(backLegSensorValues)

print('Front leg:')
print(backLegSensorValues)

p.disconnect()