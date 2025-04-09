class IDS:
    def __init__(self, map_instance):
        self.map = map_instance

    def search(self, startCityName, goalCityName):
        #Initialize start and end city and current search depth
        startCity = getattr(self.map, startCityName)
        goalCity = getattr(self.map, goalCityName)
        depthLimit = 0
        
        while True:
            #Reset visited states for each depth limit 
            visited = set()  
            path = self.dls(startCity, goalCity, depthLimit, visited, 0)
            if path is not None:
                return path
            depthLimit += 1 

    def dls(self, city, goalCity, depth, visited, currentDistance):
        if depth == 0 and city.name == goalCity.name:
            return ([city.name], currentDistance)
        if depth > 0:
            visited.add(city.name)
            for i, neighbor in enumerate(city.nextCity):
                if neighbor.name not in visited:
                    distanceToNeighbor = city.distance[i]
                    result = self.dls(neighbor, goalCity, depth - 1, visited, currentDistance + distanceToNeighbor)
                    if result is not None:
                        path, totalDistance = result
                        #Add current city to path 
                        return [city.name] + path, totalDistance  
            #Allow re-exploration for the next depth limit     
            visited.remove(city.name)  
        return None 