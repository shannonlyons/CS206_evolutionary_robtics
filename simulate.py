import constants as c
import sensor as s
import motor as m
#import world as w
import robot as r
import simulation as sim

import numpy as np
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time

from simulation import SIMULATION

class SIMULATE:
    def __init__(self):
        pass
       # self.simulation = SIMULATION()

simulation = SIMULATION()
simulation.Run()
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