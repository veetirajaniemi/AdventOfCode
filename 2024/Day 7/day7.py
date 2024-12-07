import numpy as np
from itertools import product

def checkLine(target, nums, gold = False):
    operations = [0, 1] # add, multiply
    if gold: # didn't bother to optimize this part
        operations = [0, 1, 2] # add, multiply, combine
    combos = [val for val in product(operations, repeat = len(nums) - 1)]

    for i in range(len(combos)):
        combo = combos[i]
        total = nums[0]
        for j in range(0, len(combo)):
            if combo[j] == 0:
                total += nums[j + 1]
            elif combo[j] == 1:
                total *= nums[j + 1]
            elif combo[j] == 2:
                total = int(str(total) + str(nums[j + 1]))
        if total == target:
            return True
    
    return False
       


if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()

    silver = 0
    gold = 0

    for line in lines:
        line = line[:-1]
        nums = line.split(': ')
        target = int(nums[0])
        nums = nums[1].split(' ')
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        if checkLine(target, nums):
            silver += target
        if checkLine(target, nums, True):
            gold += target

    print(silver)
    print(gold)

