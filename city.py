class city:
    def __init__ (self, n, s):
        self.name = n
        self.sld = s
        self.depth = 0
        self.cameFrom = "NULL"
        self.numConnections = 0
        self.nextCity = []
        self.distance = []

        
    def addconnection (self, c, d):
        self.numConnections += 1
        self.nextCity.append(c)
        self.distance.append(d)
        