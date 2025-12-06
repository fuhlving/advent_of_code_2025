FILE = "input.txt"
from re import sub

def task_1(content: list) -> int:
    lines = []
    
    for x in content:
        line = sub(r"\s+", " ", x)
        line = sub(r"(^\s+|\s+$)", "", line)
        line_list = line.split(" ")
        lines.append(line_list)

    dii = {}
    
    for x,_ in enumerate(lines[0]):
        dii[x] = []

    for i, x in enumerate(lines):
        for idx, val in enumerate(x):
            dii[idx].append(val)
        
    sum = 0
    for idx, x in dii.items():
        operator = x[-1:][0]
        i = 0
        for p in x[:-1]:
            p = int(p)
            if i == 0:
                i = i + p
                continue
            if operator == "*":
                i = i * p
                continue
            if operator == "+":
                i = i + p
        sum += i

    return sum


def task_2(content: list) -> int:
    dii = dict()
    operator = dict()
    i = 0
    for x in range(0, len(content[0])):
        line = []
        for l in range(0, len(content)):
            line.append(content[l][x])

        if len(set(line)) == 1:
            i += 1
            continue 
   
        num = int("".join(line[:-1]))
        
        if i not in dii.keys():
            dii[i] = []
        if line[-1:] != [" "]:
            operator[i] = line[-1:][0]
        
        dii[i].append(num)

    sum = 0
    for key, val in dii.items():
        add = 0
        for num in val:
            if operator[key] == "+":
                add += num
            if operator[key] == "*":
                if add == 0:
                    add = num
                else:
                    add = add * num
        sum += add
    
    return sum
    


def solve():
    with open(FILE) as f:
        content = f.read().splitlines()
                
    print(f"Task 1: {task_1(content)}")
    print(f"Task 2: {task_2(content)}")





    


if __name__ == "__main__":
    solve()