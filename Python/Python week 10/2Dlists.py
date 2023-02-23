

def sum1(input):
    sum = 0
    for row in range(len(input)-1):
        for col in range(len(input[0])-1):
            sum = sum + input[row][col]

    return sum


print(sum1([[1, 2], [3, 4], [5, 6]]))


def gridGenerator(w, h):
    grid = []
    for i in range(h):
        row = []
        for j in range(w):
            row.append(0)
        grid.append(row)
    return grid


def gridGenerator2(w, h):
    grid = [[0 for j in range(w)] for i in range(h)]

    return grid


def multiplicationGrid(n, h):
    table = [[0 for j in range(w)] for i in range(h)]
    for i in range(n):
        for j in range(h):
            table[i][j] = (i+1) * (j+1)
    return table


def print2DList():
    for i in range()
