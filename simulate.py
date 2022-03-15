from simulation import SIMULATION
import sys

class SIMULATE:
    def __init__(self):
        pass

directOrGui = sys.argv[1]

simulation = SIMULATION(directOrGui)
simulation.Run()
simulation.Get_Fitness()