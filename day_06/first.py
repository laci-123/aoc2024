from sys import stdin


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
                the_map[col+row*1j] = EMPTY
            case "#":      
                the_map[col+row*1j] = OBST
            case "^":      
                the_guard = (col+row*1j, 0-1j)
            case "v":      
                the_guard = (col+row*1j, 0+1j)
            case ">":      
                the_guard = (col+row*1j, 1+0j)
            case "<":      
                the_guard = (col+row*1j, -1+0j)


while True:
    position, heading = the_guard
    if 0 < position.real < width and 0 < position.imag < height:
        the_map[position] = VISITED
    else:
        break

    if the_map.get(position + heading) == OBST:
        the_guard = (position, heading * 1j)
    else:
        the_guard = (position + heading, heading)


sum = 0
for x in range(width):
    for y in range(height):
        if the_map[x + y * 1j] == VISITED:
            sum += 1
        
    
print(sum)
