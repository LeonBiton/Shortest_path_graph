import sys
from file_parser import *

infi = sys.maxsize


def dijkstraDist(nodes_list, src, path):

    dist = [infi for i in range(len(nodes_list))]
    visited = [False for i in range(len(nodes_list))]
    dist[src] = 0
    current = src

    sett = set()
    while True:
        visited[current] = True
        for i in range(len(nodes_list[current].children)):
            v = nodes_list[current].children[i].first
            if visited[v]:
                continue
            sett.add(v)
            alt = dist[current] + nodes_list[current].children[i].second

            if alt < dist[v]:
                dist[v] = alt
                path[v] = [current, nodes_list[current].children[i].second]
        if current in sett:
            sett.remove(current)
        if len(sett) == 0:
            break

        mindist = infi
        index = 0

        for a in sett:
            if dist[a] < mindist:
                mindist = dist[a]
                index = a
        current = index
    return dist


def shortest_path():
    dct = parse_file("graph.txt")
    src, dst = generate_params(dct)
    node_list = generate_graph(dct)
    print(node_list)
    path = [[] for i in range(len(dct))]
    dist = dijkstraDist(node_list, src, path)
    print("from", src, "to", dst, "cost", dist[dst])
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


