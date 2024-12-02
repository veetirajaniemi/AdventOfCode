import numpy as np


def countSimilarity(data):
    simScore = 0
    for i in range(len(data)):
        simScore += data[i,0] * np.count_nonzero(data[:,1] == data[i,0])

    return simScore


if __name__ == "__main__":
    data = np.loadtxt("input.txt")
    
    sorted = np.sort(data, axis=0)
    diffs = np.abs(sorted[:,0]-sorted[:,1])
    sums = np.sum(diffs)
    print(sums) # Part 1
    print(countSimilarity(data)) # Part 2

