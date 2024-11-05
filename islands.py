# islands.py

import heapq
from datetime import datetime

class Island:
    def __init__(self, name, population, produced_resources, natural_resources, experiences):
        self.name = name
        self.population = population
        self.produced_resources = produced_resources
        self.natural_resources = natural_resources
        self.experiences = experiences
        self.last_visited = None

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
    
    def set_last_visited(self, visit_time):
        self.last_visited = visit_time


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
        
        priority_queue = []
        
        # starting island's experiences
        first_experiences = source_node.getExperiences()
        total_time = sum(first_experiences.values())
        num_experiences = len(first_experiences)
        print(f"Starting Island: {source_node.getName()}, Total Time: {total_time}, Number of Experiences: {num_experiences}")
        print(f"Experiences: {first_experiences}")
        
        # add to queue, (total_time, num_experiences, path)
        heapq.heappush(priority_queue, (total_time, num_experiences, [source_node.getName()]))
        print("Updated priority queue: ", priority_queue)
        
        path = []
        experience_count = 0
        time = float('inf')
        
        while len(priority_queue) > 0:
            # get the item with the least total_time
            current_time, current_num_experiences, current_path = heapq.heappop(priority_queue)
            current_island = self.nodes[current_path[-1]]
            print("Pop from priority queue: ")
            print(f"Current Island: {current_island.getName()}, Current Time: {current_time}, Number of Experiences: {current_num_experiences}, Path: {' -> '.join(current_path)}")
            
            # if path to the current island is better (less time) than recorded or not in experiences
            if (current_num_experiences > experience_count or (current_num_experiences == experience_count and current_time < time)):
                print("Updating experiences for the current island")
                # update for the current island with better experiences/times
                experience_count = current_num_experiences
                time = current_time
                path = current_path
            
                # get neighboring islands
                for neighbor, route in self.edges[current_island.getName()].items():
                    print("Neighbor: ", neighbor)
                    new_time = current_time + route.getDistance()
                    neighbor_island = self.nodes[neighbor]
                    
                    # get new experiences
                    new_experiences = set(current_path)
                    for experience in neighbor_island.getExperiences().keys():
                        new_experiences.add(experience)
                    
                    update_experience_count = len(new_experiences)
                    
                    heapq.heappush(priority_queue, (new_time, update_experience_count, current_path + [neighbor]))
                    print("Updated priority queue: ", priority_queue)
        
        return path, experience_count, time

    def skills_across_islands(self, starting_island):
        # check if the starting island exists
        if starting_island not in self.nodes:
            return {}

        # initialize distances and priority queue
        distances = {island_name: float('inf') for island_name in self.nodes}
        distances[starting_island] = 0
        priority_queue = [(0, starting_island)]

        while priority_queue:
            current_distance, current_island = heapq.heappop(priority_queue)

            # update the last visited time for the current island
            self.nodes[current_island].set_last_visited(datetime.now())

            # explore neighbors
            for neighbor, route in self.edges[current_island].items():
                new_distance = current_distance + route.getDistance()
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        # prioritize islands with higher populations by storing negative population values
        prioritized_distances = {
            island_name:
            (distances[island_name], -self.nodes[island_name].population)
            for island_name in distances
        }

        # sort the distances based on the prioritized criteria
        sorted_distances = sorted(prioritized_distances.items(), key=lambda x: (x[1][0], x[1][1]))

        return {island: dist[0] for island, dist in sorted_distances}