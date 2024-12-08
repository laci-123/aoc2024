from sys import stdin
from enum import Enum


# coordinate system:
#         -1j
#          ^
#          |
#          |
# -1 <---- 0 ----> +1
#          |
#          |
#          v
#         +1j


class Cell(Enum):
    EMPTY   = 0
    OBST    = 1
    VISITED = 2


the_map = {}
the_guard = (0+0j, 0+0j) # (posittion, heading)
width = 0
height = 0


for row, line in enumerate(stdin):
    height += 1
    if width == 0:
        width = len(line.strip())
    for col, char in enumerate(line.strip()):
        match char:
            case ".":
                the_map[col+row*1j] = (Cell.EMPTY, None)
            case "#":      
                the_map[col+row*1j] = (Cell.OBST, None)
            case "^":      
                the_guard = (col+row*1j, 0-1j)
            case "v":      
                the_guard = (col+row*1j, 0+1j)
            case ">":      
                the_guard = (col+row*1j, 1+0j)
            case "<":      
                the_guard = (col+row*1j, -1+0j)


in_a_loop = 0
for y in range(height):
    for x in range(width):
        match the_map.get(x + y *1j):
            case (Cell.EMPTY, _):
                pass
            case _:
                continue
        clean_map = the_map.copy()
        clean_guard = the_guard
        clean_map[x + y *1j] = (Cell.OBST, None)
        while True:
            position, heading = clean_guard
            if 0 < position.real < width and 0 < position.imag < height:
                match clean_map.get(position):
                    case (Cell.VISITED, h) if h == heading:
                        in_a_loop += 1
                        break
                    case (Cell.EMPTY, _):
                        clean_map[position] = (Cell.VISITED, heading)
            else:
                break

            if clean_map.get(position + heading) == (Cell.OBST, None):
                clean_guard = (position, heading * 1j)
            else:
                clean_guard = (position + heading, heading)


print(in_a_loop)
