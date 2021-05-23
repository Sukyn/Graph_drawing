import random

def remove_all(l, x):
    while(x in l):
        l.remove(x)


def count_occurence(l, x):
    return l.count(x)


def random_int_list(n, bound):
    return [random.randrange(bound+1) for i in range(n)]


def random_matrix(n, bound, null_diag=False, symetric=False, oriented=False, triangular=False):
    matrix = [random_int_list(n, bound) for i in range(n)]
    if (null_diag):
        for x in range(n):
            matrix[x][x] = 0

    if (oriented):
        for i in range(n):
            for j in range(i+1,n):
                if(matrix[j][i] > 0):
                    matrix[i][j] = 0

    if (symetric):
        for x in range(n):
            for y in range(x+1, n):
                matrix[x][y] = matrix[y][x]

    if (triangular):
        for i in range(n):
            for j in range(i+1,n):
                matrix[j][i] = 0

    return matrix

def invert_permutation(permutation):
    first = permutation.copy().pop(len(permutation)-1)
    second = permutation.copy().pop(0)
    return zip(*zip(first, second).reverse())
