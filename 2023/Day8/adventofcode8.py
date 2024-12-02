def countVisibles(matrix, rows, columns):
    visibles = rows*2+columns*2-4

    for i in range(1,rows-1): # row
        for j in range(1,columns-1): # column
            fails = 0

            for k in range(0,j): # LEFT
                if matrix[i][k] >= matrix[i][j]:
                    fails += 1
                    break
        
            for k in range(j+1, columns): # RIGHT
                if matrix[i][k] >= matrix[i][j]:
                    fails += 1
                    break

            for k in range(0,i): # UP
                if matrix[k][j] >= matrix[i][j]:
                    fails += 1
                    break

            for k in range(i+1, rows): # DOWN
                if matrix[k][j] >= matrix[i][j]:
                    fails += 1
                    break

            if fails < 4:
                visibles += 1

    return visibles


def scenic(matrix, rows, columns):
    maxscenic = 0

    for i in range(1,rows-1): # row
        for j in range(1,columns-1): # column
            leftscenic = j
            rightscenic = columns-1-j
            upscenic = i
            downscenic = rows-1-i

            for k in range(j-1,0,-1): # LEFT
                
                if matrix[i][k] >= matrix[i][j]:
                    leftscenic = j-k
                    break
            
            for k in range(j+1,columns): # RIGHT
                if matrix[i][k] >= matrix[i][j]:
                    rightscenic = k-j
                    break 

            for k in range(i-1,0,-1): # UP
                if matrix[k][j] >= matrix[i][j]:
                    upscenic = i-k
                    break

            for k in range(i+1,rows): # DOWN
                if matrix[k][j] >= matrix[i][j]:
                    downscenic = k-i
                    break
            
            currscenic = leftscenic*rightscenic*upscenic*downscenic

            if (currscenic > maxscenic):
                maxscenic = currscenic

    return maxscenic


def visibles():
    input = open("input8.txt","r")
    lines = input.read().splitlines()
    columns = len(lines[0])
    rows = len(lines)
    
    
    matrix = []
    for i in range(0,rows):
        matrix.append([]) # for each row add column list
        for j in range(0,columns):
            matrix[i].append(int(lines[i][j]))

    visibles = countVisibles(matrix, rows, columns)
    maxscenic = scenic(matrix, rows, columns)

    print(f"There are {visibles} visible trees.")
    print(f"The highest scenic score possible is {maxscenic}.")

visibles()