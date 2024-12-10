from sys import stdin


def find_trail_ends(map, start, next_height = 0):
    height = map.get(start)
    if height == None or height != next_height:
        return set()
    elif height == 9:
        return {start}

    result = set()
    for z in [1, -1, 1j, -1j]:
        result = result.union(find_trail_ends(map, start + z, height + 1))

    return result


map = {}
trailheads = set()
row = -1
col = -1

for line in stdin:
    row +=1
    if col == -1:
        col = len(line.strip())

    for k, char in enumerate(line.strip()):
        height = int(char)
        point = k + row * 1j
        if height == 0:
            trailheads.add(point)
        map[point] = height


sum = 0
for trailhead in trailheads:
    sum += len(find_trail_ends(map, trailhead))


print(sum)
