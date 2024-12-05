import numpy as np

def findXMAS(matrix):
    count = 0
    for i in range(len(matrix)):
        string = ''.join(matrix[i])
        count += string.count("XMAS")
        count += string.count("SAMX")
    return count

def findMAS(matrix):
    diag1 = ''.join(np.diag(matrix))
    diag2 = ''.join(np.diag(np.fliplr(matrix)))

    if diag1 == "MAS" or diag1 == "SAM":
        if diag2 == "MAS" or diag2 == "SAM":
            return True



if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    matrix = []


    for line in lines:
        line = line[:-1]
        matrix.append(list(line))
    
    matrix = np.array(matrix)
    leftToRight = matrix
    upToDown = matrix.T

    nRows = len(matrix)
    nCols = len(matrix[0])

    diagonal = []
    diagonal2 = []

    diag_ks = list(range(-nRows + 1, nCols))

    for k in diag_ks:
        diag = np.diag(matrix, k)
        diag2 = np.diag(np.fliplr(matrix), k)
        diagonal.append(''.join(diag))
        diagonal2.append(''.join(diag2))
    

    print(findXMAS(upToDown) + findXMAS(leftToRight) + findXMAS(diagonal) + findXMAS(diagonal2)) # Part 1

    count = 0
    for i in range(nRows-2):
        for j in range(nCols-2):
            smallMatrix = matrix[i:i+3, j:j+3]
            if findMAS(smallMatrix):
                count += 1

    print(count) # Part 2
