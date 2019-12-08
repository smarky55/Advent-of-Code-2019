from common.intpc import IntPC
from itertools import permutations

phaseSet = ['0','1','2','3','4']

inFile = open('input/07.txt')
prog = inFile.readline().rstrip('\n').split(',')
inFile.close()

# Part one
maxOut = 0
for phases in permutations(phaseSet):
    lastOut = '0'
    for phase in phases:
        pc = IntPC(prog)
        pc.inQueue.append(phase)
        pc.inQueue.append(lastOut)
        pc.run()
        lastOut = pc.outQueue.popleft()
    if int(lastOut) > maxOut:
        maxOut = int(lastOut)
print(maxOut)

# Part two
phaseSet = ['5','6','7','8','9']
maxOut = 0
for phases in permutations(phaseSet):
    # construct incode pcs
    pcs = [IntPC(prog) for phase in phases]

    # Setup
    lastOutQueue = pcs[-1].outQueue
    for phase, pc in zip(phases, pcs):
        pc.inQueue = lastOutQueue
        pc.inQueue.append(phase)
        lastOutQueue = pc.outQueue
    pcs[0].inQueue.append('0')
    running = True
    while running:
        running = False
        for pc in pcs:
            running = pc.step() or running
    lastOut = pc.outQueue.popleft()
    if int(lastOut) > maxOut:
        maxOut = int(lastOut)

print(maxOut)
