from directed_graph import *

if __name__ == '__main__':
    path, src, dst = shortest_path()
    res = get_path(path, dst)
    print_path(res, dst)