from islands import *

# Initialize islands with their respective resources
new_zealand = Island("New Zealand", 1000, {"oil": 10, "wood": 75}, {"corn", "peas"}, {"nz_1": 2, "nz_2": 1})
hawaii = Island("Hawaii", 500, {"oil": 5, "sandalwood": 50}, {"papaya", "macadamia"}, {"haw_1": 4, "haw_2": 2})
maui = Island("Maui", 200, {"sugar": 10, "pineapple": 25}, {"coffee", "bananas"}, {"maui_1": 3, "maui_2": 1})

islands = CollectionOfIslands()
islands.add_island(new_zealand)
islands.add_island(hawaii)
islands.add_island(maui)

islands.add_edge(new_zealand, hawaii, 1000)
islands.add_edge(hawaii, maui, 500)
islands.add_edge(new_zealand, maui, 1500)

islands.display_graph()

# Skills distribution using Dijkstra's algorithm
distances = islands.skills_across_islands("New Zealand")

print("\nDistances for skill distribution:")
for island_name, distance in distances.items():
    print(f"Distance from New Zealand to {island_name} to distribute knowledge/skills: {distance}")

# Resource planting using Bellman-Ford algorithm
print("\nResource distribution (corn from New Zealand):")
islands.resource_planting("New Zealand", "corn")

# Check and display the updated resources on each island
print("\nUpdated resources list:")
for island_name, island in islands.nodes.items():
    print(f"{island_name}: {island.getNaturalResources()}")