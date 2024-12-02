import numpy as np

def isSafe(data):
    sortedData = np.sort(data)
    diffs = np.diff(data)

    if np.any(diffs == 0):
        return False
    
    if np.any(diffs > 3):
        return False
    
    if np.any(diffs < -3):
        return False
    

    sorted2 = np.array(sortedData[::-1])
    data = np.array(data)

    if np.array_equal(data, sortedData) or np.array_equal(data, sorted2):
        return True
    else:
        return False

    


if __name__ == "__main__":
    with open("input.txt") as f:
        safes = 0
        for line in f:
            line = line.strip()
            nums = list(map(int, line.split()))
            if isSafe(nums) == True:
                safes += 1
            else: # include for part 2
                nNums = len(nums)
                for i in range(nNums):
                    newNums = nums.copy()
                    del newNums[i]
                    if isSafe(newNums) == True:
                        safes += 1
                        break

    print(safes)