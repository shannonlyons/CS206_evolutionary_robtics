import pybullet as p

class WORLD:
    def __init__(self, myID):
      #  self.myID = myID
        filename = "world" + str(myID) + ".sdf"
        p.loadSDF(filename)
        self.planeId = p.loadURDF("plane.urdf")