from utilities import *


def get_installations_from_file(file_name):
    l = []
    file = open(file_name, 'r')
    file.readline()
    for line in file:
        line = line.strip().split('\t')
        name = line[0]
        ward = int(line[2])
        position = (float(line[7]), float(line[8]))
        if line[15] == 'INDOORS' :
            indoor = True
        else:
            indoor = False

        temp_installation = Installation (name, ward, position, indoor)
        l.append(temp_installation)

    file.close()
    return l    
    

def euclidean_distance(position1, position2):
    return ((position1[0]-position2[0])**2 + (position1[1]-position2[1])**2)**0.5


def get_adjacency_mtx(installations):
    adj = []
    for i in range (len(installations)):
        adj.append([])
        temp_source = installations[i]
        
        for j in range (len(installations)):
            #adj[i].append
            temp_compare = installations[j]
            if temp_compare.ward < temp_source.ward - 1 or temp_compare.ward > temp_source.ward + 1:
                adj[i].append(0)
            else:
                ed = euclidean_distance(temp_source.position, temp_compare.position)
                if temp_source.indoor == True or temp_compare.indoor == True:
                    ed = ed*1.5
                adj[i].append(ed)

    return adj



    

def make_graph(installations):
    
    art_installations = []
    for i in range (len(installations)):
        art_installations.append(installations[i].name)
    weighted_connect = get_adjacency_mtx(installations)
    
    
    graph = Graph(art_installations, weighted_connect)
    return graph
    


def find_shortest_path(installation_A, installation_B, graph):
    
    unvisited = []
    distance = []
    previous = {}
    for i in range (len(graph.installations)):
        unvisited.append(graph.installations[i])
        distance.append(float('inf'))
        previous [graph.installations[i]] = None
        
    distance[graph.artwork_to_index[installation_A]] = 0

    curr = installation_A

    state = True
    #while unvisited != None:
    
    while unvisited != [] :
        unvisited_distance = []
        for artwork in unvisited:
            artwork_i = graph.artwork_to_index[artwork]
            unvisited_distance.append(distance[artwork_i])
        
        mindist_node_index = unvisited_distance.index(min(unvisited_distance))
        mindist_node = unvisited.pop(mindist_node_index)
        mindist_node_index = graph.artwork_to_index[mindist_node]
        
        if mindist_node == installation_B:
            break

        
        neighbors = []
        for i in range (len (graph.installations)):
             if graph.adjacency_mtx[mindist_node_index][i] != 0 and graph.installations[i] in unvisited:
                 neighbors.append(graph.installations[i])
                 
        for artwork in neighbors:
            neighbor_i = graph.artwork_to_index[artwork]
            alt = distance [mindist_node_index] + graph.adjacency_mtx[mindist_node_index][neighbor_i]
            if alt < distance[neighbor_i]:
                distance[neighbor_i] = alt
                previous[graph.installations[neighbor_i]] = mindist_node

    shortest_distance = distance [graph.artwork_to_index[installation_B]]
    if shortest_distance == float("inf"):
        shortest_distance = None

    if previous[installation_B] == None:
        path = []
    else:
        path = []
        temp = installation_B
        while temp != None:
            path.append(temp)
            temp = previous[temp]
        path = path[::-1]
    
    tup = (shortest_distance, path)

    return tup
        

    
        
        




#if __name__ == "__main__":
    
    #installations = get_installations_from_file('test_data.txt')
    #for i in range (len(installations)):
        #print(installations[i])
    #print(euclidean_distance ((0, 0),(1, 1)))

    #print(get_adjacency_mtx(installations))

    #graph=make_graph(installations)
    #print(find_shortest_path("D", "B", graph))








   
