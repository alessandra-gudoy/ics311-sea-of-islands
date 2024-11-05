from islands import *

new_zealand = Island("New Zealand", 1000, {"oil": 10, "wood": 75}, {"corn": 10, "peas": 50}, {"nz_1": 2, "nz_2": 1})
hawaii = Island("Hawaii", 500, {"oil": 5, "sandalwood": 50}, {"papaya": 5, "macadamia": 25}, {"haw_1": 4, "haw_2": 2})
maui = Island("Maui", 200, {"sugar": 10, "pineapple": 25}, {"coffee": 5, "bananas": 20}, {"maui_1": 3, "maui_2": 1})

islands = CollectionOfIslands()
islands.add_island(new_zealand)
islands.add_island(hawaii)
islands.add_island(maui)

islands.add_edge(new_zealand, hawaii, 1000)
islands.add_edge(hawaii, maui, 500)
islands.add_edge(new_zealand, maui, 1500)

islands.display_graph()

experiences = islands.tourist_experience(new_zealand)
for island, (total_time, num_experiences, path) in experiences.items():
    print(f"Island: {island}, Total Time: {total_time}, Number of Experiences: {num_experiences}, Path: {' -> '.join(path)}")