from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("DIRECT")

        for currentGeneration in range(c.numberOfGenerations):
            print('Got here')
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        print('Got here')
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        print("**************************************************")
       # print(self.parent.weights)
        self.child.Mutate()
      #  print(self.child.weights)
      #  exit()

    def Select(self):
        print(self.parent.fitness)
        print(self.child.fitness)

        if (self.parent.fitness > self.child.fitness):
            self.parent = self.child

    def Print(self):
        print('Parent fitness: ' + self.parent.fitness + ', Child fitness:' + self.child.fitness)

    def Show_Best(self):
        self.parent