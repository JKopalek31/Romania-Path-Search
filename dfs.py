class DFS:
    def __init__(self, mapInstance):
        self.map = mapInstance

    def search(self, startCityName, goalCityName):
        #Initialize start and end city
        startCity = getattr(self.map, startCityName)
        goalCity = getattr(self.map, goalCityName)
        
        #Initialize data structure and back tracking
        stack = [(startCity, 0)] 
        visited = {startCity.name}
        cameFrom = {startCity.name: (None, 0)}  
        
        while stack:
            currentCity, currentDistance = stack.pop()  
            
            # Check if final state is reached
            if currentCity.name == goalCity.name:
                return self.reconstruct_path(cameFrom, startCity, goalCity, currentDistance)
            
            # Explore touching nodes
            for i, neighbor in enumerate(currentCity.nextCity):
                if neighbor.name not in visited:
                    visited.add(neighbor.name)
                    distanceToNeighbor = currentCity.distance[i]
                    totalDistance = currentDistance + distanceToNeighbor
                    stack.append((neighbor, totalDistance))
                    cameFrom[neighbor.name] = (currentCity.name, totalDistance)
        
        return None 

    #Make output readable
    def reconstruct_path(self, cameFrom, startCity, goalCity, totalDistance):
        path = []
        current = goalCity.name
        
        while current is not None:
            path.append(current)
            current = cameFrom[current][0]
        
        path.reverse()  
        return path, totalDistance  
