FILE = "input.txt"

def task(input: str, max_digits=12) -> int:
    int_li = [int(x) for x in input]
    int_li_s = list(set(int_li.copy()))
    int_li_s.sort(reverse=True)
    
    high_num_int = int()
    start = 10**(max_digits - 1)
    digits = 0

    while digits < max_digits:
        for digit in int_li_s:
            if digit not in int_li:
                continue
            digit_pos = int_li.index(digit)
            if len(int_li[digit_pos:]) >= max_digits - digits:
                int_li = int_li[digit_pos+1:]
                high_num_int = high_num_int + digit * start
                start = int(start/10)
                digits = digits + 1
                break
    return high_num_int

def solve() -> None:
    with open(FILE) as f:
        content = f.readlines()
    
    content = [x.strip() for x in content]
    num_1 = 0
    num_2 = 0
    for x in content:
        num_1 += task(x, max_digits=2)
        num_2 += task(x)

    print(f"Task 1: {num_1}")
    print(f"Task 2: {num_2}")

if __name__ == "__main__":
    solve()