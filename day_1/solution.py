FILE = "input.txt"
from math import floor

with open(FILE) as f:
    content = f.readlines()

def solve(content: list[str]) -> tuple[int,int]:
    dial = 50
    p2_count = 0
    p1_count = 0
    for x in content:
        direction, num = x[0], int(x[1:])
        rot = floor(num/100)
        p2_count = p2_count + rot
        num = num % 100
        if direction == "R":
            dial = dial + num
        else:
            dial = dial - num

        if dial == 100 or dial == 0:
            p1_count += 1
            dial = 0
            continue

        if dial > 100:
            p2_count += 1
            dial = dial - 100
        
        if dial < 0:
            if dial + num != 0:
                p2_count += 1
            dial = dial + 100
        
    return (p1_count, p1_count + p2_count)

if __name__ == "__main__":
    p1, p2 = (solve(content))

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
