

class IntPC:
    def __init__(self, memory):
        self.memory = list(memory)
        self.pc = 0

    def run(self):
        while 1:
            instr = self.memory[self.pc]
            opc, modeStr = self.decode(instr)
            if opc == 1:
                modes = self.getModes(modeStr, 3)
                self.add(modes)
            elif opc == 2:
                modes = self.getModes(modeStr, 3)
                self.mul(modes)
            elif opc == 3:
                self.read()
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
            elif opc == 99:
                break
            else:
                print('Error!')
                break


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

    def fetch(self, add, mode=1):
        if mode == 0:
            return int(self.memory[int(self.memory[add])])
        elif mode == 1:
            return int(self.memory[add])

    def store(self, add, data, mode=1):
        if mode == 0:
            self.memory[int(self.memory[add])] = str(data)
        elif mode == 1:
            self.memory[add] = str(data)

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

    def read(self):
        data = int(input())
        self.store(self.pc+1, data, 0)
        self.pc += 2

    def print(self, mode):
        print(self.fetch(self.pc+1, mode[0]))
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