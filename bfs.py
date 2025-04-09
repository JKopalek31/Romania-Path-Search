class BFS:
    def __init__(self, mapInstance):
        self.map = mapInstance

    def search(self, startCityName, goalCityName):
        startCity = getattr(self.map, startCityName)
        goalCity = getattr(self.map, goalCityName)
        
        #Initialize data structures and backtracking
        queue = [(startCity, 0)]
        visited = {startCity.name}
        cameFrom = {startCity.name: (None, 0)}
        
        while queue:
            currentCity, currentDistance = queue.pop(0)
            
            #Check if goal is met
            if currentCity.name == goalCity.name:
                return self.reconstructPath(cameFrom, startCity, goalCity, currentDistance)
            
            #Explore touching nodes
            for i, neighbor in enumerate(currentCity.nextCity):
                if neighbor.name not in visited:
                    visited.add(neighbor.name)
                    distanceToNeighbor = currentCity.distance[i]
                    totalDistance = currentDistance + distanceToNeighbor
                    queue.append((neighbor, totalDistance))
                    cameFrom[neighbor.name] = (currentCity.name, totalDistance)
        
        return None

    #Change output for readabiliy
    def reconstructPath(self, cameFrom, startCity, goalCity, totalDistance):
        path = []
        current = goalCity.name
        
        while current is not None:
            path.append(current)
            current = cameFrom[current][0]
        
        path.reverse()  
        return path, totalDistance 

