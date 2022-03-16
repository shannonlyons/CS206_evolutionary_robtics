import os
from hillclimber import HILL_CLIMBER

import hillclimber as hc

# class SEARCH:
#     def __init__(self):
#         print('********* Got here in search.py *********')
#         self.hc.Evolve()

os.system("python3 hillclimber.py")

hc = HILL_CLIMBER()
hc.Evolve()
hc.Show_Best()

#os.system("python3 generate.py")
#os.system("python3 simulate.py")
