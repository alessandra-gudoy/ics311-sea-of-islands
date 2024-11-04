class Island:
    def __init__(self, name, population, produced_resources, natural_resources):
        self.name = name
        self.population = population
        self.produced_resources = produced_resources
        self.natural_resources = natural_resources

    def getName(self):
        return self.name

    def getPopulation(self):
        return self.population
    
    def getProducedResources(self):
        return self.produced_resources
    
    def getNaturalResources(self):
        return self.natural_resources

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

    def add_edge(self, from_island, to_island, weight):
        if from_island in self.nodes and to_island in self.nodes:
            self.edges[from_island][to_island] = weight

    def display_graph(self):
        for from_island, connections in self.edges.items():
            for to_island, weight in connections.items():
                print(f"{from_island} -> {to_island} with weight {weight}")

