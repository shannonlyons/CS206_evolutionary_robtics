import numpy as np
import pybullet as p
import pybullet_data

class CONSTANTS:
    def __init__(self):

        self.backLegSensorValues = np.zeros(1000)
        self.frontLegSensorValues = np.zeros(1000)

        self.targetAngles = np.linspace(-np.pi, 2*np.pi, 1000)

        self.back_amplitude = -np.pi / 4
        self.front_amplitude = np.pi / 4

        self.back_frequency = 0.06
        self.front_frequency = -0.06

        self.back_phaseOffset = 0
        self.front_phaseOffset = 0
