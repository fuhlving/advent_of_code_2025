FILE = "input.txt"

from re import match

def task_1(numbers: list, ranges: list[range]) -> int:
    sum = 0

    for num in numbers:
        for r in ranges:
            if num in r:
                sum += 1
                break
    
    return sum 

def task_2(ranges: list[range]) -> int:
    while True:
        unchanged = True
        for idx, rng in enumerate(ranges):
            for iidx, irng in enumerate(ranges):
                if (rng.start or rng.stop) in irng:
                    if idx == iidx:
                        continue
                    new_start = min(rng.start, irng.start)
                    new_stop = max(rng.stop, irng.stop)
                    ranges[iidx] = range(new_start, new_stop)
                    ranges.pop(idx)

                    unchanged = False
                    break
        
        if unchanged:
            break

    sum = 0
    for x in ranges:
        sum += len(x)
    
    return sum

def solve():
    with open(FILE) as f:
        content = f.read().splitlines()

    ranges = []
    numbers = []
    
    for x in content:
        if match(r"^[0-9]+\-[0-9]+$", x):
            range_in_content = x.split("-")
            ranges.append(range(int(range_in_content[0]), int(range_in_content[1]) +1))
        if match(r"^[0-9]+$", x):
            numbers.append(int(x))

    ranges = list(set(ranges))
    ranges.sort(key=lambda r: r.start)


    print(f"Task 1: {task_1(numbers, ranges)}")
    print(f"Task 2: {task_2(ranges)}")
            

if __name__ == "__main__":
    solve()