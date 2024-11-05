class Island:
    """
        str name - name of the island
        int population - population of the island
        dictionary produced_resources - resources that the island produces
                                         key = resource name, value = amount
        dictionary natural_resources - resources that the island has
                                        key = resource name, value = amount
        dictionary experiences - experiences that the island has
                                  key = experience name, value = time
    """
        
    def __init__(self, name, population, produced_resources, natural_resources, experiences):
        self.name = name
        self.population = population
        self.produced_resources = produced_resources
        self.natural_resources = natural_resources
        self.experiences = experiences

    def getName(self):
        return self.name

    def getPopulation(self):
        return self.population
    
    def getProducedResources(self):
        return self.produced_resources
    
    def getNaturalResources(self):
        return self.natural_resources
      
    def getExperiences(self):
        return self.experiences

class Route:
    def __init__(self, from_island, to_island, distance):
        self.from_island = from_island
        self.to_island = to_island
        self.distance = distance

    def getFromIsland(self):
        return self.from_island

    def getToIsland(self):
        return self.to_island

    def getDistance(self):
        return self.distance

class CollectionOfIslands:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_island(self, island):
        if island.getName() not in self.nodes:
            self.nodes[island.getName()] = island
            self.edges[island.getName()] = {}

    def add_edge(self, from_island, to_island, distance):
        if from_island.getName() in self.nodes and to_island.getName() in self.nodes:
            route = Route(from_island, to_island, distance)
            self.edges[from_island.getName()][to_island.getName()] = route

    def display_graph(self):
        for from_island, connections in self.edges.items():
            for to_island, route in connections.items():
                print(f"{from_island} -> {to_island} with distance {route.getDistance()}")

