import os
import numpy as np

from parallelHillClimber import PARALLEL_HILL_CLIMBER

os.system("python3 parallelHillClimber.py")

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()

np.save('resultsA', phc.resultsA)
np.savetxt('resultsA', phc.resultsA)

#os.system("python3 generate.py")
#os.system("python3 simulate.py")
