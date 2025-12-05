FILE = "input.txt"
import textwrap

def task_1(input: str) -> bool:
    for key in range(len(input)):
        key = key + 1
        if input[:key] == input[key:]:
            return True
    return False

def task_2(input: str) -> int:
    le = len(input)
    for x in range(1, le):
        if le % x == 0:
            if len(set(textwrap.wrap(input, x))) == 1:
                return int(input)
    return 0

def solve() -> None:
    num_1 = 0
    num_2 = 0
    with open(FILE) as f:
        content = f.read()
    
    content = content.split(",")

    for x in content:
        range_start, range_end = x.split("-")
        for x in range(int(range_start), int(range_end) +1):
            if task_1(str(x)):
                num_1 += x
            
            num_2 += task_2(str(x))
    
    print(f"Task 1: {num_1}")
    print(f"Task 2: {num_2}")

if __name__ == "__main__":
    solve()