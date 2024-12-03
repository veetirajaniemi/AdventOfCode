def multiply(data, gold = False):
    disabled = False
    val = 0

    for i in range(len(lines)):
        if gold:
            if lines[i:i+7] == 'don\'t()':
                disabled = True
                continue

            if disabled:
                if lines[i:i+4] == 'do()':
                    disabled = False
                continue

        if lines[i:i+4] == 'mul(':
            toSplit = lines[i+4:]
            num1 = toSplit.split(',')[0]

            if num1.isdigit():
                num1 = int(num1)    
                num2 = toSplit.split(',')[1].split(')')[0]
                if num2.isdigit():
                    num2 = int(num2)
                    val += num1 * num2 
    
    return val


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    lines = ''.join(lines)
    print(multiply(lines)) # part 1
    print(multiply(lines, True)) # part 2
    




            