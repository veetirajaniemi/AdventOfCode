

def checkLine(line, dict, gold = False):
    for i in range(len(line)): # 0 1 2 3 4
        if i < len(line) + 1: 
            for j in range(i+1, len(line)): 
                if int(line[j]) in dict[int(line[i])]['mustBeAfter']:
                    if gold:
                        line[j], line[i] = line[i], line[j]
                        return checkLine(line, dict, gold = True)    
                    return False
        if i > 0:
            for j in range(i):
                if int(line[j]) in dict[int(line[i])]['mustBeBefore']:
                    if gold:
                        line[j], line[i] = line[i], line[j]
                        return checkLine(line, dict, gold = True)
                    return False
    return True


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    dict = {}
    keys = ['mustBeBefore', 'mustBeAfter']

    silver = 0
    gold = 0
    x = 0

    for line in lines:
        line = line[:-1]
        
        if len(line) > 0:
            if line[2] == '|':
                num1 = int(line[0:2])
                num2 = int(line[3:5])

                if num1 not in dict:
                    dict[num1] = {key: [] for key in keys}
                dict[num1]['mustBeBefore'].append(num2)

                if num2 not in dict:
                    dict[num2] = {key: [] for key in keys}
                dict[num2]['mustBeAfter'].append(num1)

            else:
                line = line.split(',')
                for i in range(len(line)):
                    line[i] = int(line[i])

                
                if checkLine(line, dict):
                    middleNum = line[len(line) // 2]
                    silver += middleNum
                else:
                    if checkLine(line, dict, gold = True):
                        middleNum = line[len(line) // 2]
                        gold += middleNum

    print(silver)
    print(gold)