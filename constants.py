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

numberOfGenerations = 1
populationSize = 1

numSensorNeurons = 3
numMotorNeurons = 2