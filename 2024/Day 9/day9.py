
def createBlock(line):
    block = []

    id = 0
    addId = True
    for i in range(len(line)):
        if addId:
            for j in range(int(line[i])):
                block.append(str(id))
            addId = False
            id += 1
        else:
            for j in range(int(line[i])):
                block.append('.')
            addId = True

    return block


def reorderBlock(block):
    changes = block.count('.')
    lastIndex = -1
    firstIndex = 0

    while lastIndex > -1 * changes - 1:
        if block[lastIndex] == '.':
            lastIndex -= 1
        else:
            while block[firstIndex] != '.':
                firstIndex += 1
            block[lastIndex], block[firstIndex] = block[firstIndex], block[lastIndex]

    return block

def checkSum(block):
    count = 0
    for i in range(len(block)):
        if block[i] == '.':
            continue
        else:
            count += (i * int(block[i]))
    return count

def reOrderBlock2(block):
    

    def findFirst(block, firstIndex = 0):
        firstSpace = 1
        curId = block[firstIndex]
        
        for i in range(firstIndex, len(block)):
            if block[i] == '.':
                firstIndex = i
                curId = block[i]
                break

        for i in range(firstIndex + 1, len(block)):
            if block[i] == curId:
                firstSpace += 1
            else:
                break

        return firstIndex, firstSpace
    
    def findLast(block, currLastIndex):
        lastSpace = 0
        curId = block[currLastIndex]
        while block[currLastIndex] == '.':
            currLastIndex -= 1
            curId = block[currLastIndex]
        while block[currLastIndex] == curId:
            currLastIndex -= 1
            lastSpace += 1
        currLastIndex += lastSpace
        return currLastIndex, lastSpace


    lastIndex = -1
    lastSpace = 0
    tried = []
    blockVals = []
    for i in range(len(block)):
        if block[i] != '.' and block[i] != '0' and block[i] not in blockVals:
            blockVals.append(block[i])


    for i in range(len(blockVals)): # check all ids to change
        firstIndex, firstSpace = findFirst(block)
        lastIndex, lastSpace = findLast(block, lastIndex - lastSpace)

        while block[lastIndex] in tried:
            lastIndex, lastSpace = findLast(block, lastIndex - lastSpace)
        tried.append(block[lastIndex])


        if lastSpace <= firstSpace and firstIndex < len(block) + lastIndex - lastSpace + 1: # if room to change (that was the stupid line that took me 2 days to figure out)
            for i in range(lastSpace):
                block[firstIndex + i] = block[lastIndex - i]
                block[lastIndex - i] = '.'
        else: 
            while lastSpace > firstSpace:  # no room to change
                firstIndex, firstSpace = findFirst(block, firstIndex + firstSpace)   

                if firstIndex >= len(block) + lastIndex - lastSpace + 1:                     
                    break
        
                if lastSpace <= firstSpace: # room to change
                    for i in range(lastSpace):
                        block[firstIndex + i] = block[lastIndex - i]
                        block[lastIndex - i] = '.'
                    break

    return block




if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()

    for line in lines:
        line = line[:-1]
        line = list(line)

    block = createBlock(line)
    block2 = block.copy()


    reOrdered1 = reorderBlock(block)
    print(checkSum(reOrdered1)) # part 1

    reOrdered2 = reOrderBlock2(block2)
    print(checkSum(reOrdered2)) # part 2
