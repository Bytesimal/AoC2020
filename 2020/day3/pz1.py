import numpy as np


class Env:
    def __init__(self, path):
        tmp_pattern = []
        with open(path) as f:
            line = f.readline().strip()
            while line != "":
                tmp_pattern.append(line)
                line = f.readline().strip()

        self.width = len(tmp_pattern[0])
        self.depth = len(tmp_pattern)

        # create np array
        self.pattern = np.empty((self.depth, self.width), dtype=np.object)
        for r, row in enumerate(tmp_pattern):
            for c, val in enumerate(row):
                self.pattern[r, c] = val

    def at_coord(self, x, y):
        res_x = int(x - np.floor(x / self.width) * self.width)
        return self.pattern[y, res_x]


def traverse(env, *traverse_vector):
    nx, ny = 0, 0
    n_trees = 0

    while ny < env.depth:
        if env.at_coord(nx, ny) == "#":
            n_trees += 1

        nx += traverse_vector[0]
        ny += traverse_vector[1]

    return n_trees


environment = Env("input.txt")


def main():
    print(traverse(environment, 3, 1))


if __name__ == "__main__":
    main()
