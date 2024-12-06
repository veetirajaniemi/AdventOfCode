import numpy as np

def countLocations(matrix, gold = False):
    locations = []
    dir = 'N'
    loc = np.where(matrix == '^')
    loc = (loc[0][0], loc[1][0])
    locations.append(loc)

    turns = []

    while True:
        


        if dir == 'N':
            if loc[0] - 1 < 0:
                return locations
            if matrix[loc[0] - 1, loc[1]] == '#':
                dir = 'E'
                if loc != locations[-1]:
                    turns.append(loc)
            elif matrix[loc[0] - 1, loc[1]] == 'O':
                dir = 'E'
                if loc != locations[-1]:
                    turns.append(loc)
            else:
                loc = (loc[0] - 1, loc[1])

        elif dir == 'E':
            if loc[1] + 1 > len(matrix[0]) - 1:
                return locations
            if matrix[loc[0], loc[1] + 1] == '#':
                dir = 'S'
                if loc != locations[-1]:
                    turns.append(loc)
            elif matrix[loc[0], loc[1] + 1] == 'O':
                dir = 'S'
                if loc != locations[-1]:
                    turns.append(loc)
            else: 
                loc = (loc[0], loc[1] + 1)
            
        elif dir == 'S':
            if loc[0] + 1 > len(matrix) - 1:
                return locations
            if matrix[loc[0] + 1, loc[1]] == '#':
                dir = 'W'
                if loc != locations[-1]:
                    turns.append(loc)
            elif matrix[loc[0] + 1, loc[1]] == 'O':
                dir = 'W'
                if loc != locations[-1]:
                    turns.append(loc)
            else:
                loc = (loc[0] + 1, loc[1])

        elif dir == 'W':
            if loc[1] - 1 < 0:
                return locations
            if matrix[loc[0], loc[1] - 1] == '#':
                dir = 'N'
                if loc != locations[-1]:
                    turns.append(loc)
            elif matrix[loc[0], loc[1] - 1] == 'O':
                dir = 'N'
                if loc != locations[-1]:
                    turns.append(loc)
            else:
                loc = (loc[0], loc[1] - 1)
        
        if loc not in locations:
            locations.append(loc)
        
        if loc in locations and turns.count(loc) >= 2 and gold:
            return True



if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    matrix = []
    for line in lines:
        line = line[:-1]
        matrix.append(list(line))
    matrix = np.array(matrix)

    
    skip = False

    locations = countLocations(matrix)
    part1 = len(locations)

    print(f"Part 1: {part1}")

    gold = 0

    nCols = len(matrix[0])
    nRows = len(matrix)



    # Fucked the optimization up, so I'm just gonna BRUTEE FORCEEEEE it
    # (to fix)
    # ((tbh never coming back to this code, it's a mess))

    for i in range(1, len(locations)):
    #     skipLoc = False
    #     if tuple(map(lambda j, k: j - k, locations[i], locations[i-1])) == (1, 0): # one down, so we need to look left
    #         for j in range(0, locations[i-1][1] + 1):                
    #             if matrix[locations[i-1][0] + 1,j] == '#': # there is a wall so we can't go further
    #                 skipLoc = True
    #                 break

    #     elif tuple(map(lambda j, k: j - k, locations[i], locations[i-1])) == (-1, 0): # one up, so we need to look right
    #         for j in range(locations[i-1][1], nCols):
    #             if matrix[locations[i-1][0] + 1,j] == '#':
    #                 skipLoc = True
    #                 break

    #     elif tuple(map(lambda j, k: j - k, locations[i], locations[i-1])) == (0, 1): # going right, so we need to look down
            
    #         for j in range(locations[i-1][0], nRows):
    #             if matrix[j, locations[i-1][1]] == '#':
    #                 skipLoc = True
    #                 break

        
    #     elif tuple(map(lambda j, k: j - k, locations[i], locations[i-1])) == (0, -1): # going left, so we need to look up
    #         for j in range(locations[i-1][0], -1, -1):
    #             if matrix[j, locations[i-1][1] + 1] == '#':
    #                 skipLoc = True
    #                 break

    #     if skipLoc:
    #         continue
    #     else:

        newObstacle = locations[i]
        newMatrix = matrix.copy()
        newMatrix[newObstacle] = 'O'

        if countLocations(newMatrix, gold = True) == True:
            gold += 1

    print(f"Part 2: {gold}")

