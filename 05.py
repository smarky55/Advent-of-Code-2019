from common.intpc import IntPC

with open('input/05.txt') as inFile:
    data = inFile.readline().split(',')
    pc = IntPC(data)
    pc.run()