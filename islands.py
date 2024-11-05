from heapq import heapify, heappop, heappush

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
    
    def tourist_experience(self, source_node):
        print(f"Starting experience route from {source_node.getName()}")
        
        experiences = {}
        priority_queue = []
        
        # starting island's experiences
        first_experiences = source_node.getExperiences()
        total_time = sum(first_experiences.values())
        num_experiences = len(first_experiences)
        print(f"Starting Island: {source_node.getName()}, Total Time: {total_time}, Number of Experiences: {num_experiences}")
        print(f"Experiences: {first_experiences}")
        
        # store the starting island's experience info
        experiences[source_node.getName()] = (total_time, num_experiences, [source_node.getName()])
        
        # add to queue, (total_time, num_experiences, path)
        heappush(priority_queue, (total_time, num_experiences, [source_node.getName()]))
        print("Updated priority queue: ", priority_queue)
        
        while len(priority_queue) > 0:
            # get the item with the least total_time
            current_time, current_num_experiences, current_path = heappop(priority_queue)
            current_island = self.nodes[current_path[-1]]
            print("Pop from priority queue: ")
            print(f"Current Island: {current_island.getName()}, Current Time: {current_time}, Number of Experiences: {current_num_experiences}, Path: {' -> '.join(current_path)}")
            
            # if path to the current island is better (less time) than recorded or not in experiences
            if (current_island.getName() not in experiences or current_time < experiences[current_island.getName()][0]):
                print("Updating experiences for the current island")
                # update experiences for the current island
                experiences[current_island.getName()] = (current_time, current_num_experiences, current_path)
            
                # experiences of the current island and add them to the queue
                for exp, exp_time in current_island.getExperiences().items():
                    update_time = current_time + exp_time
                    update_num_experiences = current_num_experiences + 1
                    update_path = current_path + [current_island.getName()]
                    
                    heappush(priority_queue, (update_time, update_num_experiences, update_path))
                
                # get neighboring islands
                for neighbor, route in self.edges[current_island.getName()].items():
                    new_time = current_time + route.getDistance()
                    neighbor_island = self.nodes[neighbor]
                    
                    if neighbor not in experiences or (new_time < experiences[neighbor][0]):
                        new_path = current_path + [neighbor]
                        heappush(priority_queue, (new_time, current_num_experiences, new_path))
        
        return experiences