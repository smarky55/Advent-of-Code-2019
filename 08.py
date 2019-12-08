
width = 25
height = 6


inFile = open('input/08.txt')
#data = '0222112222120000'
data = inFile.readline().rstrip('\n')
inFile.close()


image = []

for i, digit in enumerate(data):
    n = int(digit)
    if i % (width * height) == 0:
        image.append([])
    layerNum = i // (width*height)
    image[layerNum].append(n)

minZeros = width * height + 1
minZeroLayer = 0
for i, layer in enumerate(image):
    if layer.count(0) < minZeros:
        minZeros = layer.count(0)
        minZeroLayer = i

print(image[minZeroLayer].count(1) * image[minZeroLayer].count(2))

decoded = [0] * width * height

for i in range(width * height):
    for layer in image:
        if layer[i] == 2:
            continue
        decoded[i] = layer[i]
        break

for j in range(height):
    for i in range(width):
        print(decoded[i+j*width], end=' ')
    print('')