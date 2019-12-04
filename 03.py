from common.vector import Vector
import math

def points(moves):
    pos = Vector()
    positions = [Vector(pos)]
    for move in moves:
        direction = move[0]
        distance = int(move[1:])
        if (direction == 'U'):
            pos.y += distance
        elif direction == "R":
            pos.x += distance
        elif direction == "D":
            pos.y -= distance
        else:
            pos.x -= distance
        positions.append(Vector(pos))
    return positions

def isUpDown(start, end):
    return Vector.angle(end-start, Vector(0,1)) % math.pi == 0

def isBetween(x, a, b):
    return a<=x<=b or a>=x>=b

def intersects(start1, end1, start2, end2):
    if isUpDown(start1, end1) == isUpDown(start2, end2):
        return None # Parallel lines
    
    if isUpDown(start1, end1):
        if isBetween(start1.x, start2.x, end2.x) and isBetween(start2.y, start1.y, end1.y):
            return [start1.x, start2.y]
    else:
        if isBetween(start1.y, start2.y, end2.y) and isBetween(start2.x, start1.x, end1.x):
            return [start2.x, start1.y]
    return None

def wireLengthToPoint(points, point):
    dist = 0
    pos = points[0]
    for nextPos in points[1:]:
        if isUpDown(pos, nextPos) and pos.x == point.x and isBetween(point.y, pos.y, nextPos.y):
            dist += abs(point.y - pos.y)
            return dist
        elif not isUpDown(pos, nextPos) and pos.y == point.y and isBetween(point.x, pos.x, nextPos.x):
            dist += abs(point.x - pos.x)
            return dist
        else:
            dist += abs(Vector.distance(pos, nextPos))
            pos = nextPos

inFile = open('input/03.txt')
points1 = points(inFile.readline().split(','))
points2 = points(inFile.readline().split(','))
inFile.close()
intersections = []

for start1, end1 in zip(points1[:-1], points1[1:]):
    for start2, end2 in zip(points2[:-1], points2[1:]):
        # print(start1, end1, start2, end2)
        intersection = intersects(start1, end1, start2, end2)
        if (intersection and intersection != Vector(0,0)):
            intersections.append(intersection)

print(intersections)
absInters = []
for intersection in intersections:
    absInters.append(map(abs, intersection))
minDistance = min(map(sum, absInters))
print(minDistance)

minDistance = 9999999
for point in intersections:
    dist = wireLengthToPoint(points1, Vector(point)) + wireLengthToPoint(points2, Vector(point))
    if dist < minDistance:
        minDistance = dist
print(minDistance)