import sys


# def print_map(tiles, visited, cell, heading, width, height):
#     for y in range(height):
#         for x in range(width):
#             z = x + y * 1j
#             if z == cell:
#                 match heading:
#                     case 1:
#                         print(">", end="")
#                     case -1j:
#                         print("^", end="")
#                     case -1:
#                         print("<", end="")
#                     case 1j:
#                         print("v", end="")
#             elif z in tiles:
#                 if z in visited:
#                     print("_", end="")
#                 else:
#                     print(".", end="")
#             else:
#                 print("#", end="")
#         print("")


def step(tiles, visited, cell, heading, end, score, width, height):
    # print_map(tiles, visited, cell, heading, width, height)
    # print(score)
    # print("")
    if cell == end:
        return score

    if cell not in visited or score < visited[cell]:
        visited[cell] = score
    else:
        return None
    
    s_1, s_2, s_3 = None, None, None
    if cell + heading in tiles:
        s_1 = step(tiles, visited, cell + heading, heading, end, score + 1, width, height)
    if cell + heading * (-1j) in tiles:
        s_2 = step(tiles, visited, cell + heading * (-1j), heading * (-1j), end, score + 1001, width, height)
    if cell + heading * 1j in tiles:
        s_3 = step(tiles, visited, cell + heading * 1j, heading * 1j, end, score + 1001, width, height)

    s = [s for s in [s_1, s_2, s_3] if s != None]
    if s == []:
        return None
    else:
        return min(s)


tiles = set()
start = 0
end = 0
heading = 1

y = 0
for line in sys.stdin:
    x = 0
    for char in line.strip():
        cell = x + y * 1j
        match char:
            case ".":
                tiles.add(cell)
            case "S":
                start = cell
                tiles.add(cell)
            case "E":
                end = cell
                tiles.add(cell)
        x += 1
    y += 1


sys.setrecursionlimit(10000)
print(step(tiles, {}, start, heading, end, 0, x, y))
