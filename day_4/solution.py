FILE = "input.txt"

def remove_paper(grid: list[list[str]]) -> tuple[int, list[list[str]]]:
    GRID_WIDTH = len(grid[0])
    GRID_HEIGHT = len(grid)
    next_grid = []
    for x in grid:
        next_grid.append(x.copy())
    
    rolls = 0

    for x_pos, li in enumerate(grid):
        for y_pos, inner_li in enumerate(li):
            if inner_li != "@":
                continue
            num = 0
            # Check above
            if x_pos > 0:
                if grid[x_pos - 1][y_pos] == "@":
                    num += 1
            # Check below
            if x_pos < GRID_HEIGHT - 1:
                if grid[x_pos + 1][y_pos] == "@":
                    num += 1
            # Check behind
            if y_pos > 0:
                # Current row
                if grid[x_pos][y_pos - 1] == "@":
                    num += 1                
                # Row abowe
                if x_pos > 0:
                    if grid[x_pos - 1][y_pos -1] == "@":
                        num += 1
                # Row below
                if x_pos < GRID_HEIGHT - 1:
                    if grid[x_pos + 1][y_pos -1] == "@":
                        num += 1
            # Check in front
            if y_pos < GRID_WIDTH - 1:
                # Current row
                if grid[x_pos][y_pos + 1] == "@":
                    num += 1                
                # Row abowe
                if x_pos > 0:
                    if grid[x_pos - 1][y_pos + 1] == "@":
                        num += 1
                # Row below
                if x_pos < GRID_HEIGHT - 1:
                    if grid[x_pos + 1][y_pos + 1] == "@":
                        num += 1

            if num < 4:
                rolls += 1
                next_grid[x_pos][y_pos] = "."
    
    return (rolls, next_grid)

def solve():
    with open(FILE) as f:
        content = f.read().splitlines()

    # Construct grid
    grid = []
    for x in content:
        grid.append([l for l in x])
    
    sum_1, sum_2 = 0, 0

    while True:
        removed_rolls, grid = remove_paper(grid)
        if sum_1 == 0:
            sum_1 = removed_rolls
        sum_2 += removed_rolls

        if removed_rolls == 0:
            break

    print(f"Task 1: {sum_1}")
    print(f"Task 2: {sum_2}")

if __name__ == "__main__":
    solve()