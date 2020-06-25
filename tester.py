from dja import *
from utilities import *

if __name__ == "__main__":
    A = Installation("A", 5, (1, 1), True)
    B = Installation("B", 4, (1, 2), False)
    C = Installation("C", 3, (2, 2), False)
    D = Installation("D", 2, (2, 5), False)
    E = Installation("E", 2, (2, 4), True)
    installations = [A, B, C, D, E]

    print("Testing get_adjacency_mtx:")
    print(get_adjacency_mtx(installations))
    print("")

    print("Testing make_graph:")
    graph = make_graph(installations)
    print("graph.installations:")
    print(graph.installations)
    print("graph.adjacency_mtx:")
    print(graph.adjacency_mtx)
    print("graph.artwork_to_index:")
    print(graph.artwork_to_index)
    print("")

    print("Testing find_shortest_path:")
    print(find_shortest_path("A", "B", graph))
    print(find_shortest_path("C", "A", graph))
    print(find_shortest_path("D", "B", graph))
    print(find_shortest_path("A", "E", graph))
    print("")


    installations = get_installations_from_file('test_data.txt')
    for installation in installations:
        print(installation)

    graph = make_graph(installations)
    print(graph)


    installations = get_installations_from_file('public_artwork_data.txt')
    graph = make_graph(installations)
    installation_A = 'GALAXY'
    installation_B = 'MIRAGE'
    distance, path = find_shortest_path(installation_A, installation_B, graph)

    print("The shortest path between {} and {} is {} along nodes:".format(installation_A,installation_B, str(distance)))
    for node in path:
        print(node)
