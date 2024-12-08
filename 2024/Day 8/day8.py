import numpy as np
from scipy.spatial.distance import cdist

def antiNodes(data, nRows, nCols, gold = False):
    found = []
    antiNodes = []


    for i in range(len(data)):
        if data[i] != '.' and data[i] not in found:
            found.append(data[i])
            indices = np.where(data == data[i])[0]

            if gold and len(indices) >= 3:
                for j in range(len(indices)):
                    if indices[j] not in antiNodes:
                        antiNodes.append(indices[j])


            for j in range(len(indices - 1)):
                for k in range(j + 1, len(indices)):
                    diff = indices[k] - indices[j]
                    
                    firstLoc = np.unravel_index(indices[j], (nRows, nCols))
                    secondLoc = np.unravel_index(indices[k], (nRows, nCols))

                    if gold:
                        diffRow = secondLoc[0] - firstLoc[0]
                        diffCol = secondLoc[1] - firstLoc[1]
                        currLoc = [firstLoc[0], firstLoc[1]]
                        currLoc2 = currLoc.copy()

                        while True:
                            currLoc[0] += diffRow
                            currLoc[1] += diffCol

                            if currLoc[0] < 0 or currLoc[0] >= nRows or currLoc[1] < 0 or currLoc[1] >= nCols:
                                break
                            index = np.ravel_multi_index(currLoc, (nRows, nCols))
                            if index not in antiNodes:
                                antiNodes.append(index)

                        while True:
                            currLoc2[0] -= diffRow
                            currLoc2[1] -= diffCol
                            if currLoc2[0] < 0 or currLoc2[0] >= nRows or currLoc2[1] < 0 or currLoc2[1] >= nCols:
                                break
                            index = np.ravel_multi_index(currLoc2, (nRows, nCols))
                            if index not in antiNodes:
                                antiNodes.append(index)

                            

                    if indices[j] - diff >= 0 and indices[j] - diff not in antiNodes:
                        loc = np.unravel_index(indices[j] - diff, (nRows, nCols))
                        if cdist([loc], [firstLoc], metric='cityblock') == cdist([firstLoc], [secondLoc], metric='cityblock'):
                            antiNodes.append(indices[j] - diff)

                    if indices[k] + diff < len(data) and indices[k] + diff not in antiNodes:
                        loc = np.unravel_index(indices[k] + diff, (nRows, nCols))
                        if cdist([firstLoc], [secondLoc], metric='cityblock') == cdist([secondLoc], [loc], metric='cityblock'):
                            antiNodes.append(indices[k] + diff)

    return len(antiNodes)


                


if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()

    data = []
    first = True
    for line in lines:
        if first:
            first = False
            nCols = len(line[:-1])
        for val in line[:-1]:
            data.append(val)

    nRows = len(lines)
    data = np.array(data)
    print(antiNodes(data, nRows, nCols))
    print(antiNodes(data, nRows, nCols, True))