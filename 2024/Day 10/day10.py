import numpy as np


def countPathsGold(matrix, loc):
    dirs = ['N', 'E', 'S', 'W']
    
    if matrix[loc[0], loc[1]] == 8:
        curcount = 0
        for i in range(len(dirs)):
            if dirs[i] == 'N' and loc[0] != 0:
                if matrix[loc[0]-1, loc[1]] == 9:
                    curcount += 1  
            
            elif dirs[i] == 'E' and loc[1] != len(matrix[0])-1:
                if matrix[loc[0], loc[1]+1] == 9:
                    curcount += 1

            elif dirs[i] == 'S' and loc[0] != len(matrix)-1:
                if matrix[loc[0]+1, loc[1]] == 9:
                    curcount += 1

            elif dirs[i] == 'W' and loc[1] != 0:
                if matrix[loc[0], loc[1]-1] == 9:
                    curcount += 1
            
        return curcount


    else:
        result = 0
        for i in range(len(dirs)):
            if dirs[i] == 'N' and loc[0] != 0:
                if matrix[loc[0]-1, loc[1]] == matrix[loc[0], loc[1]]+1:
                    result += countPathsGold(matrix, (loc[0]-1, loc[1]))
            
            elif dirs[i] == 'E' and loc[1] != len(matrix[0])-1:
                if matrix[loc[0], loc[1]+1] == matrix[loc[0], loc[1]]+1:
                    result += countPathsGold(matrix, (loc[0], loc[1]+1))

            elif dirs[i] == 'S' and loc[0] != len(matrix)-1:
                if matrix[loc[0]+1, loc[1]] == matrix[loc[0], loc[1]]+1:
                    result += countPathsGold(matrix, (loc[0]+1, loc[1]))

            elif dirs[i] == 'W' and loc[1] != 0:
                if matrix[loc[0], loc[1]-1] == matrix[loc[0], loc[1]]+1:
                    result += countPathsGold(matrix, (loc[0], loc[1]-1))
        
        return result


def countPaths(matrix, loc, found):
    dirs = ['N', 'E', 'S', 'W']
    
    if matrix[loc[0], loc[1]] == 8:
        curcount = 0
        for i in range(len(dirs)):
            if dirs[i] == 'N' and loc[0] != 0:
                if matrix[loc[0]-1, loc[1]] == 9:
                    if (loc[0]-1, loc[1]) not in found:
                        found.append((loc[0]-1, loc[1]))
                        curcount += 1
                    
            
            elif dirs[i] == 'E' and loc[1] != len(matrix[0])-1:
                if matrix[loc[0], loc[1]+1] == 9:
                    if (loc[0], loc[1]+1) not in found:
                        found.append((loc[0], loc[1]+1))
                        curcount += 1

            elif dirs[i] == 'S' and loc[0] != len(matrix)-1:
                if matrix[loc[0]+1, loc[1]] == 9:
                    if (loc[0]+1, loc[1]) not in found:
                        found.append((loc[0]+1, loc[1]))
                        curcount += 1

            elif dirs[i] == 'W' and loc[1] != 0:
                if matrix[loc[0], loc[1]-1] == 9:
                    if (loc[0], loc[1]-1) not in found:
                        found.append((loc[0], loc[1]-1))
                        curcount += 1
            
        return curcount


    else:
        result = 0
        for i in range(len(dirs)):
            if dirs[i] == 'N' and loc[0] != 0:
                if matrix[loc[0]-1, loc[1]] == matrix[loc[0], loc[1]]+1:
                    result += countPaths(matrix, (loc[0]-1, loc[1]), found)
            
            elif dirs[i] == 'E' and loc[1] != len(matrix[0])-1:
                if matrix[loc[0], loc[1]+1] == matrix[loc[0], loc[1]]+1:
                    result += countPaths(matrix, (loc[0], loc[1]+1), found)

            elif dirs[i] == 'S' and loc[0] != len(matrix)-1:
                if matrix[loc[0]+1, loc[1]] == matrix[loc[0], loc[1]]+1:
                    result += countPaths(matrix, (loc[0]+1, loc[1]), found)

            elif dirs[i] == 'W' and loc[1] != 0:
                if matrix[loc[0], loc[1]-1] == matrix[loc[0], loc[1]]+1:
                    result += countPaths(matrix, (loc[0], loc[1]-1), found)
        
        return result


if __name__ == "__main__":
    with open('input.txt') as f:
        data = f.readlines()

    matrix = []
    for line in data:
        line = line[:-1]
        line = list(line)
        line = [int(i) for i in line]
        matrix.append(line)

    matrix = np.array(matrix)
    locations = []


    for i in range(len(matrix)):
        col = np.where(matrix[i] == 0)[0]
        row = i
        for j in range(len(col)):
            locations.append((row, col[j]))

    silver = 0
    gold = 0

    for i in range(len(locations)):
        found = []
        add = countPaths(matrix, locations[i], found)
        add2 = countPathsGold(matrix, locations[i])
        silver += add
        gold += add2
    
    print(f'silver: {silver}')
    print(f'gold: {gold}')





    

        
    