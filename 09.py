from common.intpc import IntPC

inFile = open('input/09.txt')
data = inFile.readline().strip().split(',')
inFile.close()

# Part one
pc = IntPC(data)
pc.inQueue.append('1')
pc.run()
print(pc.outQueue)

# Part two
pc = IntPC(data)
pc.inQueue.append('2')
pc.run()
print(pc.outQueue)