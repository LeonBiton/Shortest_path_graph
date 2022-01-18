import ast


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


class Node:
    def __init__(self, vertex_number):
        self.vertexNumber = vertex_number
        self.children = []

    def add_child(self, number, length):
        p = Pair(number, length)
        self.children.append(p)


def parse_file(file_name):
    file = open(file_name, 'r')
    contents = file.read()
    dictionary = ast.literal_eval(contents)

    file.close()
    return dictionary


def generate_params(dict):
    src = dict['params']['src']
    dst = dict['params']['dst']
    if (src not in dict) or (dst not in dict):
        raise ValueError('Invalid Input')
    del dict['params']
    return src, dst


def generate_graph(dict):
    res = []
    for key in dict:
        a = Node(key)
        #print(key, '->', dict[key])
        for vertex in dict[key]:
            a.add_child(vertex, dict[key][vertex])
        res.append(a)
    return res

