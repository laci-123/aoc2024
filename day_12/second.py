from sys import stdin


neighbours = [0 + 1j, 0 - 1j, 1 + 0j, -1 + 0j]

def calculate_region(map, start, kind, region):
    region.add(start)
    area = 1
    for z in neighbours:
        cell = start + z
        if cell not in region and map.get(cell) == kind:
            area += calculate_region(map, cell, kind, region)
    return area


def count_corners(region, cell):
    diagonals = [1 + 1j, 1 - 1j, -1 + 1j, -1 -1j]
    corners = 0
    for z in diagonals:
        n = cell + z
        if n not in region:
            if n - z.real in region and n - z.imag * 1j in region:
                corners += 1
            elif n - z.real not in region and n - z.imag * 1j not in region:
                corners += 1
        elif n in region:
            if n - z.real not in region and n - z.imag * 1j not in region:
                corners += 1
    return corners


def calculate_sides(region):
    sides = 0
    for cell in region:
        sides += count_corners(region, cell)
    return sides


map = {}
row = 0
for line in stdin:
    col = 0
    for char in line.strip():
        cell = col + row * 1j
        map[cell] = char
        col += 1
    row += 1


price = 0
processed = set()
for cell, kind in map.items():
    if cell not in processed:
        region = set()
        area = calculate_region(map, cell, kind, region)
        sides = calculate_sides(region)
        price += area * sides
        processed = processed.union(region)


print(price)
