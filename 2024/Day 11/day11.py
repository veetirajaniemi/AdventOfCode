

def blink(dict):

    newDict = {} # new dictionary to store values
    for key in dict.keys(): 

        if key == 0:
            if 1 not in newDict.keys():
                newDict[1] = 0
            newDict[1] += dict[key]

        elif len(str(key)) % 2 == 0: # even number of digits
            key = str(key)
            firstVal = int(key[:len(key)//2]) # first half
            secondVal = int(key[len(key)//2:]) # second half

            if firstVal not in newDict.keys():
                newDict[firstVal] = 0
            if secondVal not in newDict.keys():
                newDict[secondVal] = 0
            
            key = int(key)

            newDict[firstVal] += dict[key]
            newDict[secondVal] += dict[key]


        else: # val * 2024
            if key * 2024 not in newDict.keys():
                newDict[key * 2024] = 0
            newDict[key * 2024] += dict[key]
            
    return newDict




if __name__ == "__main__":
    with open('input.txt') as f:
        data = f.readlines()

    for line in data:
        line = line[:-1]

    vals = (list(line.split(' ')))
    vals = [int(i) for i in vals]
    totalCount = 0

    valDict = {key: 1 for key in vals}
    
    for i in range(1, 76):
        valDict = blink(valDict)
        if i == 25:
            silver = sum(valDict.values())
  
    gold = sum(valDict.values())
    
    print("Silver: ", silver)
    print("Gold: ", gold)
