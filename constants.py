import numpy as np

targetAngles = np.linspace(-np.pi, 2*np.pi, 1000)
amplitude = np.pi / 4
frequency = 0.06
offset = 0

back_amplitude = -np.pi / 4
front_amplitude = np.pi / 4

back_frequency = 0.06
front_frequency = -0.06

back_phaseOffset = 0
front_phaseOffset = 0

numberOfGenerations = 4
populationSize = 4

numSensorNeurons = 4
numMotorNeurons = 8

motorJointRange = 0.2