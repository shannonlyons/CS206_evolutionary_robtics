import constants as c
import sensor as s
import motor as m
import world as w
import robot as r

import numpy as np
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time

from simulation import SIMULATION

class SIMULATE:
    def __init__(self):
        self.simulation = SIMULATION()

    def Run(self):
        self.back_sin_array = []
        self.front_sin_array = []

        for e in range(len(c.targetAngles)):
            self.back_sin_array.append(c.back_amplitude * np.sin((c.back_frequency * e) + c.back_phaseOffset))

        for e in range(len(c.targetAngles)):
           self.front_sin_array.append(c.front_amplitude * np.sin((c.front_frequency * e) + c.front_phaseOffset))

        # sin_array = []
        # for e in targetAngles:
        #     sin_array.append(np.sin(e))

        #np.save('data/targetAngles.npy', back_sin_array)
        #np.save('data/targetAngles.npy', front_sin_array)

        for i in range (1000):
            print(i)
            # p.stepSimulation()
            # c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            # pyrosim.Set_Motor_For_Joint(r.robotId, "Torso_BackLeg", p.POSITION_CONTROL, self.back_sin_array[i], 20)
            # pyrosim.Set_Motor_For_Joint(r.robotId, "Torso_FrontLeg", p.POSITION_CONTROL, self.front_sin_array[i], 20)
            # time.sleep(1/120)

  #  simulate.Run()
#
# # save here
# np.save('data/backLegSensorValues.npy', backLegSensorValues)
# np.save('data/frontLegSensorValues.npy', frontLegSensorValues)
#
# print('Back leg:')
# print(backLegSensorValues)
#
# print('Front leg:')
# print(backLegSensorValues)
#
# p.disconnect()