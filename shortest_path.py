import sys
from file_parser import *

infi = sys.maxsize


def dijkstraDist(nodes_list, src, path):

    distance = [infi for i in range(len(nodes_list))]
    visited = [False for i in range(len(nodes_list))]
    distance[src] = 0
    current = src

    #set of all childrens
    sett = set()
    while True:
        visited[current] = True
        #iterate all current node childrens
        for i in range(len(nodes_list[current].children)):
            vertex = nodes_list[current].children[i].first
            if visited[vertex]:
                continue
            sett.add(vertex)
            alt = distance[current] + nodes_list[current].children[i].second

            if alt < distance[vertex]:
                distance[vertex] = alt
                path[vertex] = [current, nodes_list[current].children[i].second]
        if current in sett:
            sett.remove(current)
        if len(sett) == 0:
            break

        min_distance = infi
        index = 0

        #iterate set and find the smallest dist
        for a in sett:
            if distance[a] < min_distance:
                min_distance = distance[a]
                index = a
        current = index
    return distance


def shortest_path():
    dct = parse_file("graph.txt")
    src, dst = generate_params(dct)
    node_list = generate_graph(dct)
    path = [[] for i in range(len(dct))]
    dist = dijkstraDist(node_list, src, path)
    #print("from", src, "to", dst, "cost", dist[dst])
    return path, src, dst


def get_path(path,dst):
    res = [infi for i in range(len(path)*2)]
    i = 0
    d = dst
    while True:
        res[i] = path[d][0]
        res[i+1] = path[d][1]
        i = i + 2
        d = path[d][0]
        if not path[d]:
            return res


def print_path(path,dst):
    res = list(filter((infi).__ne__, path))
    i = len(res) - 1
    while i >= 0:
        print(res[i-1], "--", "({})".format(res[i]), "--> ", end='')
        i = i - 2
    print(dst, end='')


