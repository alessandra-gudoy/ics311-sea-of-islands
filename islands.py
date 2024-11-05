import heapq
from datetime import datetime

class Island:
    def __init__(self, name, population, produced_resources, natural_resources, experiences):
        self.name = name
        self.population = population
        self.produced_resources = produced_resources
        self.natural_resources = set(natural_resources)  # Store natural resources as a set of strings
        self.experiences = experiences
        self.last_visited = None

    def getName(self):
        return self.name

    def getPopulation(self):
        return self.population

    def getProducedResources(self):
        return self.produced_resources

    def getNaturalResources(self):
        return list(self.natural_resources)

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

    def skills_across_islands(self, starting_island):
        if starting_island not in self.nodes:
            return {}
        distances = {island_name: float('inf') for island_name in self.nodes}
        distances[starting_island] = 0
        priority_queue = [(0, starting_island)]
        while priority_queue:
            current_distance, current_island = heapq.heappop(priority_queue)
            self.nodes[current_island].set_last_visited(datetime.now())
            for neighbor, route in self.edges[current_island].items():
                new_distance = current_distance + route.getDistance()
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))
        prioritized_distances = {
            island_name: (distances[island_name], -self.nodes[island_name].population)
            for island_name in distances
        }
        sorted_distances = sorted(prioritized_distances.items(), key=lambda x: (x[1][0], x[1][1]))
        return {island: dist[0] for island, dist in sorted_distances}

    def resource_planting(self, source, resource):
        distances = {node: float('inf') for node in self.nodes}
        distances[source] = 0
        predecessors = {node: None for node in self.nodes}
        
        if resource not in self.nodes[source].natural_resources:
            self.nodes[source].natural_resources.add(resource)
        
        for _ in range(len(self.nodes) - 1):
            for u in self.edges:
                for v, route in self.edges[u].items():
                    if distances[u] + route.getDistance() < distances[v]:
                        distances[v] = distances[u] + route.getDistance()
                        predecessors[v] = u
        
        for u in self.edges:
            for v, route in self.edges[u].items():
                if distances[u] + route.getDistance() < distances[v]:
                    print("Graph contains a negative-weight cycle")
                    return
        
        print(f"Initial resources at {source}: {self.nodes[source].natural_resources}")
        for node in self.nodes:
            if node != source:
                print(f"Distributing {resource} to {node}")
                current = node
                path = []
                while current != source:
                    path.append(current)
                    current = predecessors[current]
                path.append(source)
                path.reverse()
                print(f"Path taken: {' -> '.join(path)}")
                for island in path:
                    if island != source:
                        self.nodes[island].natural_resources.add(resource)
                print(f"Canoe returning to {source} for more resources.")

        return distances
