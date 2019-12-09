from collections import deque

class IntPC:
    def __init__(self, memory):
        self.memory = list(memory)
        self.pc = 0
        self.rb = 0
        self.inQueue  = deque()
        self.outQueue = deque()

    def run(self):
        while self.step():
            pass

    def step(self):
        instr = self.memory[self.pc]
        opc, modeStr = self.decode(instr)
        if opc == 1:
            modes = self.getModes(modeStr, 3)
            self.add(modes)
        elif opc == 2:
            modes = self.getModes(modeStr, 3)
            self.mul(modes)
        elif opc == 3:
            modes = self.getModes(modeStr, 1)
            self.read(modes)
        elif opc == 4:
            modes = self.getModes(modeStr, 1)
            self.print(modes)
        elif opc == 5:
            modes = self.getModes(modeStr, 2)
            self.jumpIfTrue(modes)
        elif opc == 6:
            modes = self.getModes(modeStr, 2)
            self.jumpIfFalse(modes)
        elif opc == 7:
            modes = self.getModes(modeStr, 3)
            self.lessThan(modes)
        elif opc == 8:
            modes = self.getModes(modeStr, 3)
            self.equal(modes)
        elif opc == 9:
            modes = self.getModes(modeStr, 1)
            self.rbAdd(modes)
        elif opc == 99:
            return False
        else:
            print('Error!')
            return False
        return True

    def decode(self, instr):
        opc = 0
        mode = ''
        if len(instr) == 1:
            opc = int(instr)
        else:
            opc = int(instr[-2:])
            mode = instr[:-2]
        return opc, mode
    
    def getModes(self, modeStr, numArgs):
        modes = [0]*numArgs
        for i, mode in enumerate(reversed(modeStr)):
            modes[i] = int(mode)
        return modes

    def alloc(self, addr):
        if addr >= len(self.memory):
            self.memory.extend([0] * (1 + addr - len(self.memory)))

    def fetch(self, add, mode=1):
        self.alloc(add)
        if mode == 0:
            self.alloc(int(self.memory[add]))
            return int(self.memory[int(self.memory[add])])
        elif mode == 1:
            return int(self.memory[add])
        elif mode == 2:
            self.alloc(self.rb + int(self.memory[add]))
            return int(self.memory[self.rb + int(self.memory[add])])

    def store(self, add, data, mode=1):
        self.alloc(add)
        if mode == 0:
            self.alloc(int(self.memory[add]))
            self.memory[int(self.memory[add])] = str(data)
        elif mode == 1:
            self.memory[add] = str(data)
        elif mode == 2:
            self.alloc(self.rb + int(self.memory[add]))
            self.memory[self.rb + int(self.memory[add])] = str(data)

    def add(self, mode):
        a = self.fetch(self.pc+1, mode[0])
        b = self.fetch(self.pc+2, mode[1])
        self.store(self.pc+3, a+b, mode[2])
        self.pc += 4

    def mul(self, mode):
        a = self.fetch(self.pc+1, mode[0])
        b = self.fetch(self.pc+2, mode[1])
        self.store(self.pc+3, a*b, mode[2])
        self.pc += 4

    def read(self, modes):
        # Only do something if we have data to read
        # This is semi blocking, it returns but doesn't advance the PC
        if len(self.inQueue) > 0:
            data = self.inQueue.popleft()
            self.store(self.pc+1, data, modes[0])
            self.pc += 2

    def print(self, mode):
        self.outQueue.append(self.fetch(self.pc+1, mode[0]))
        self.pc += 2

    def jumpIfTrue(self, mode):
        cond = self.fetch(self.pc+1, mode[0])
        add = self.fetch(self.pc+2, mode[1])
        if cond != 0:
            self.pc = add
        else:
            self.pc += 3

    def jumpIfFalse(self, mode):
        cond = self.fetch(self.pc+1, mode[0])
        add = self.fetch(self.pc+2, mode[1])
        if cond == 0:
            self.pc = add
        else:
            self.pc += 3

    def lessThan(self, modes):
        a = self.fetch(self.pc+1, modes[0])
        b = self.fetch(self.pc+2, modes[1])
        if a < b:
            self.store(self.pc+3, 1, modes[2])
        else:
            self.store(self.pc+3, 0, modes[2])
        self.pc += 4

    def equal(self, modes):
        a = self.fetch(self.pc+1, modes[0])
        b = self.fetch(self.pc+2, modes[1])
        if a == b:
            self.store(self.pc+3, 1, modes[2])
        else:
            self.store(self.pc+3, 0, modes[2])
        self.pc += 4

    def rbAdd(self, modes):
        a = self.fetch(self.pc+1, modes[0])
        self.rb += a
        self.pc += 2