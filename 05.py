from common.intpc import IntPC

with open('input/05.txt') as inFile:
    data = inFile.readline().split(',')
    pc = IntPC(data)
    pc.inQueue.append(input())
    pc.run()
    while(len(pc.outQueue)):
        print(pc.outQueue.popleft())