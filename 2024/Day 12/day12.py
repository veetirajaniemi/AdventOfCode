import numpy as np


def countRegion(matrix, start, starts, checked, area, perimeter):
    toCheck = [] # list of tuples of positions to check
    starts.append(start)
    checked.append(start)
    plot = matrix[start]
    row = start[0]
    col = start[1]


    if row > 0: # let's check up
        if matrix[row - 1][col] == plot:
            if (row - 1, col) not in checked:
                toCheck.append((row - 1, col))
                area += 1
        else:
            perimeter += 1
        checked.append((row - 1, col))
    else:
        perimeter += 1

    if col > 0: # let's check left
        if matrix[row][col - 1] == plot:
            if (row, col - 1) not in checked:
                toCheck.append((row, col - 1))
                area += 1
        else:
            perimeter += 1
        checked.append((row, col - 1))
    else:
        perimeter += 1
    
    if col < len(matrix[0]) - 1: # let's check right
        if matrix[row][col + 1] == plot:
            if (row, col + 1) not in checked:
                toCheck.append((row, col + 1))
                area += 1
        else:
            perimeter += 1
        checked.append((row, col + 1))
    else:
        perimeter += 1

    if row < len(matrix) - 1: # let's check down
        if matrix[row + 1][col] == plot:
            if (row + 1, col) not in checked:
                toCheck.append((row + 1, col))
                area += 1
        else:
            perimeter += 1
        checked.append((row + 1, col))
    else:
        perimeter += 1


    for location in toCheck:
        starts, area, perimeter, checked = countRegion(matrix, location, starts, checked, area, perimeter)
        

    return starts, area, perimeter, checked



if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()

    matrix = []
    for line in lines:
        line = line[:-1]
        matrix.append(list(line))

    matrix = np.array(matrix)
    starts = [] # list of tuples of start positions
    silver = 0
    gold = 0
    prevStarts = 0
    nRows = len(matrix)
    nCols = len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            start = (i, j)
            perimeter = 0
            area = 1
            if start not in starts:
                checked = [] # list of tuples of checked positions for this region
                starts, area, perimeter, checked = countRegion(matrix, start, starts, checked, area, perimeter)
                allStarts = len(starts)
                curStarts = allStarts - prevStarts
                curLocs = starts[prevStarts:allStarts]
                prevStarts = allStarts
                silver += area * perimeter


    print(f"Silver: {silver}")

