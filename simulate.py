import pybullet as p
import numpy as np
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

p.loadSDF("world.sdf")
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(500)
frontLegSensorValues = np.zeros(500)
#print(backLegSensorValues)
for i in range (500):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    #print(backLegTouch)
    time.sleep(1/60)
    #print(i)

# save here
np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)

print('Back leg:')
print(backLegSensorValues)

print('Front leg:')
print(backLegSensorValues)

p.disconnect()