
class node:
    def __init__(self, id):
        self.id = id
        self.children = []
        self.parent = None

    def addChild(self, child):
        self.children.append(child)
        child.setParent(self)

    def setParent(self, parent):
        self.parent = parent

    def countOrbits(self, depth=0):
        nOrbits = depth
        for child in self.children:
            nOrbits += child.countOrbits(depth+1)
        return nOrbits

    def path(self):
        path = [self]
        if self.parent:
            return path + self.parent.path()
        else:
            return path

nodes = {}

inFile = open('input/06.txt')
orbits = inFile.readlines()
orbits = [s.rstrip('\n') for s in orbits]
inFile.close()

# Could do both these loops in one but it runs fast enough already
for pair in orbits:
    a, b = pair.split(')')
    if a not in nodes:
        nodes[a] = node(a)
    if b not in nodes:
        nodes[b] = node(b)

for pair in orbits:
    a, b = pair.split(')')
    nodes[a].addChild(nodes[b])

print(nodes['COM'].countOrbits())

pathToSAN = nodes['SAN'].path()
pathToYOU = nodes['YOU'].path()

print(list(zip(reversed([node.id for node in pathToSAN]), reversed([node.id for node in pathToYOU]))))

while len(pathToSAN) > 0 and len(pathToYOU) > 0:
    if pathToSAN[-1] == pathToYOU[-1]:
        pathToSAN.pop()
        pathToYOU.pop()
    else:
        break
print(len(pathToSAN) + len(pathToYOU) - 2)