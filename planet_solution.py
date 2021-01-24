import numpy as np
from Graph import *

def planet (file_input):
    # text processing
    text = open(file_input).read().split('\n')
    line0 = text[0].split()
    
    message1 = 'The cordinates must be in between -10000 and 10000'
    message2 = 'The number of station must be in between 1 and 5000'
    # zearth coordinate
    zearth = [float(a) for a in line0]
    for elt in zearth:
        if elt < 10000 and elt > -10000:
            pass
        else:
            print(message1)
            return
    # number of stations
    station_num = int(text[1])
    if 1<station_num<5000:
        pass
    else:
        print(message2)
        return
    earth =[0.0, 0.0, 0.0]
    station_list = []
    station_list.append(earth)
    station_list.append(zearth)

    # station coordinate's extraction
    for line in text[2:]:
        l = line.split()
        station_i = [float(a) for a in l]
        for elt in station_i:
            if elt < 10000 and elt > -10000:
                pass
            else:
                print(message1)
                return 
        station_list.append(station_i)

    # distance between two stations
    distance = lambda point1, point2: np.linalg.norm(np.asarray(point1) - np.asarray(point2))

    # construction of the graph
    graph = Graph(station_num +2) #origin and end point

    # feeding graph with weight and position of each station
    for i,p1 in enumerate(station_list):
        for j,p2 in enumerate(station_list):
            if (i !=j) and (i>j):
                weight = distance(p1,p2)
                graph.add_edge(i,j,weight)

    # set of minimum spanning tree
    result = graph.find_MST()

    # shortest path going from earth to zearth
    path = graph.find_shortest_path(0,1,result)

    # getting the maximum weight of the best path
    weight_max = graph.get_max_weight(path)

    print(np.round(weight_max, 2))
    
planet('task1_test1.txt')
planet('task1_test2.txt')
