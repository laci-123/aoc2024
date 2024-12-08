from sys import stdin


# coordinate system:
#   0 ----> +1 (x)
#   |
#   |
#   v
#  +1
#  (y)


UP    = (0, -1)
RIGHT = (1, 0)
DOWN  = (0, 1)
LEFT  = (-1, 0)


def rotate(heading):
    if heading == UP:
        return RIGHT
    if heading == RIGHT:
        return DOWN
    if heading == DOWN:
        return LEFT
    if heading == LEFT:
        return UP


def move(position, heading):
    return (position[0] + heading[0], position[1] + heading[1])


obstacles = set()
the_guard = ((0, 0), (0, 0)) # (posittion, heading)
width = 0
height = 0


for row, line in enumerate(stdin):
    height += 1
    if width == 0:
        width = len(line.strip())
    for col, char in enumerate(line.strip()):
        match char:
            case "#":      
                obstacles.add((col, row))
            case "^":      
                the_guard = ((col, row), UP)
            case "v":      
                the_guard = ((col, row), DOWN)
            case ">":      
                the_guard = ((col, row), RIGHT)
            case "<":      
                the_guard = ((col, row), LEFT)


in_a_loop = 0

for y in range(height):
    for x in range(width):
        point = (x, y)
        if point in obstacles or point == the_guard[0]:
            continue
        
        guard = the_guard
        obstacles.add(point)
        visited = {}

        while True:
            position, heading = guard
            if 0 < position[0] < width and 0 < position[1] < height:
                is_visited = visited.get(position)
                if is_visited == heading:
                    in_a_loop += 1
                    break
                elif is_visited == None:
                    visited[position] = heading
            else:
                break

            next_point = move(position, heading)
            if next_point in obstacles:
                guard = (position, rotate(heading))
            else:
                guard = (next_point, heading)

        obstacles.remove(point)


print(in_a_loop)
