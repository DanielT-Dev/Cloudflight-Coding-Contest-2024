n = 0
answer = 0

def write_output(results):
    with open("output.txt", "w") as file:
        for r in results:
            file.write(f"{r}\n")

def read_input_and_solve():
    global answer

    results = []
    with open("input.txt", "r") as file:
        n = int(file.readline().strip())
        for _ in range(n):
            cols, rows = map(int, file.readline().strip().split())
        
            results.append((cols // 3) * rows)
    
    write_output(results)


read_input_and_solve()
