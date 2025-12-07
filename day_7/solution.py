FILE = "input.txt"

from functools import cache

task_1 = 0

@cache
def check_collision(x:int ,y:int):
    global task_1
    if x >= len(content):
        return 1
    if content[x][y] == "^":
        task_1 += 1
        return check_collision(x, y - 1) + check_collision(x, y + 1)

    return check_collision(x + 1, y)
    
    
def solve() -> None:
    global content
    with open(FILE) as f:
        content = f.read().splitlines()

    start = content[0].find("S")

    task_2 = check_collision(1, start)
    print(f"Task 1: {task_1}")
    print(f"Task 2: {task_2}")


if __name__ == "__main__":
    solve()