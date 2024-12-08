from sys import stdin
from itertools import combinations


def within_bounds(z, width, height):
    return 0 <= z.real < width and 0 <= z.imag < height


frequncies = {}
width = 0
height = 0

for y, line in enumerate(stdin):
    height += 1
    if width == 0:
        width = len(line.strip())
    for x, char in enumerate(line.strip()):
        if char != ".":
            point = x + y * 1j
            if char in frequncies:
                frequncies[char].append(point)
            else:
                frequncies[char] = [point]


nodes = set()
for freq, antennas in frequncies.items():
    for x, y in combinations(antennas, 2):
        x_to_y = y - x
        distance = abs(x_to_y)
        node_1 = x - x_to_y
        node_2 = y + x_to_y
        if within_bounds(node_1, width, height):
            nodes.add(node_1)
        if within_bounds(node_2, width, height):
            nodes.add(node_2)


print(len(nodes))
