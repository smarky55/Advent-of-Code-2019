
def run(mem):
    pc = 0
    while 1:
        op = mem[pc]
        if (op == 1):
            mem[mem[pc+3]] = mem[mem[pc+1]] + mem[mem[pc+2]]
        elif (op == 2):
            mem[mem[pc+3]] = mem[mem[pc+1]] * mem[mem[pc+2]]
        elif (op == 99):
            break
        pc += 4


with open('02/input.txt') as inFile:
    inp = inFile.readline().split(',')
    inp = list(map(int, inp))
    
    for i in range(0, 99):
        for j in range(0, 99):
            mem = list(inp)
            mem[1] = i
            mem[2] = j
            run(mem)
            if mem[0] == 19690720:
                print(i, j, 100 * i + j)
                break
            
