# import numpy as np
# import matplotlib.pyplot as plt
#
# backLegSensorValues = np.load('data/backLegSensorValues.npy')
# frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
#
# print(backLegSensorValues)
# print(frontLegSensorValues)
#
# plt.plot(backLegSensorValues, label='Back Leg', linewidth=5)
# plt.plot(frontLegSensorValues, label='Front Leg')
#
# # Plot target Angles
# targetAngles = np.load('data/targetAngles.npy')
# print (targetAngles)
# plt.plot(targetAngles, np.sin(targetAngles))
#
# plt.legend()
# plt.show()




from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

rows = [1, 2, 3, 4, 5]
fitnessA = np.load('resultsA.npy')
fitnessB = np.load('resultsB.npy')

meanOfA = np.mean(fitnessA, axis=1)
meanOfB = np.mean(fitnessB, axis=1)
stdOfA = np.std(fitnessA, axis=1)
stdOfB = np.std(fitnessB, axis=1)

meanPlusStdA = (meanOfA + (stdOfA))
meanMinusStdA = (meanOfA - (stdOfA))
meanPlusStdB = (meanOfB + (stdOfB))
meanMinusStdB = (meanOfB - (stdOfB))

plt.plot(meanPlusStdA, label='(M + S): Hexapod A = 2L2R')
plt.plot(meanOfA, label='(M): Hexapod A = 2F2B')
plt.plot(meanMinusStdA, label='(M - S): Hexapod A = 2L2R')
#
plt.plot(meanPlusStdB, label='(M + S): Hexapod B = 3L3R')
plt.plot(meanOfB, label='(M): Hexapod B = 2L2R')
plt.plot(meanMinusStdB, label='(M - S): Hexapod B = 3L3R')

# plt.plot(fitnessA, label='Hexapod A: 2L2R', linewidth=3)
# plt.plot(fitnessB, label='Hexapod B: 3L3R')

# plt.plot(stdOfA, label)
# plt.plot(meanOfB, label='ROBOT B')

# for col in range(fitnessFunctionA.shape[1]):
#     plt.plot(rows, fitnessFunctionA[:, col], label='(A)generation'+str(col+1))

# for col in range(fitnessFunctionB.shape[1]):
#     plt.plot(rows, fitnessFunctionB[:, col], label='(B)generation'+str(col+1))

plt.legend()
plt.show()