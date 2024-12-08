from sys import stdin


# coordinate system:
#  0 ----> +1
#  |
#  |
#  v
# +1j


obstacles = set()
the_guard = (0+0j, 0+0j) # (posittion, heading)
width = 0
height = 0


for row, line in enumerate(stdin):
    height += 1
    if width == 0:
        width = len(line.strip())
    for col, char in enumerate(line.strip()):
        match char:
            case "#":      
                obstacles.add(col+row*1j)
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
        point = x + y * 1j
        if point in obstacles or point == the_guard[0]:
            continue
        
        guard = the_guard
        obstacles.add(point)
        visited = {}

        while True:
            position, heading = guard
            if 0 < position.real < width and 0 < position.imag < height:
                is_visited = visited.get(position)
                if is_visited == heading:
                    in_a_loop += 1
                    break
                elif is_visited == None:
                    visited[position] = heading
            else:
                break

            next_point = position + heading
            if next_point in obstacles:
                guard = (position, heading * 1j)
            else:
                guard = (next_point, heading)

        obstacles.remove(point)


print(in_a_loop)
