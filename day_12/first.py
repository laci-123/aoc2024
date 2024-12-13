from sys import stdin


neighbours = [0 + 1j, 0 - 1j, 1 + 0j, -1 + 0j]

def calculate_region(map, start, kind, region):
    region.add(start)
    area = 1
    perimeter = 4 - sum([(2 if start + z in region else 0) for z in neighbours])
    for z in neighbours:
        cell = start + z
        if cell not in region and map.get(cell) == kind:
            a, p = calculate_region(map, cell, kind, region)
            area += a
            perimeter += p
    return (area, perimeter)


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
        area, perimeter = calculate_region(map, cell, kind, region)
        price += area * perimeter
        processed = processed.union(region)

print(price)
