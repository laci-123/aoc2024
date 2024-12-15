from sys import stdin


def move(walls, boxes, robot, step):
    target = robot + step
    while target in boxes:
        target += step

    if target in walls:
        return robot
    else:
        new_robot = robot + step
        if new_robot in boxes:
            boxes.remove(new_robot)
            boxes.add(target)
        return new_robot


def calculate_gps(boxes):
    gps = 0
    for box in boxes:
        gps += 100 * int(box.imag) + int(box.real)
    return gps


walls = set()
boxes = set()
robot = 0

reading_map = True
y = 0
while reading_map:
    line = next(stdin)
    x = 0
    for char in line:
        match char:
            case "#":
                walls.add(x + y * 1j)
            case "O":
                boxes.add(x + y * 1j)
            case "@":
                robot = x + y * 1j
            case "\n":
                if x == 0:
                    reading_map = False
                    break
        x += 1
    y += 1


for line in stdin:
    for char in line.strip():
        match char:
            case ">":
                robot = move(walls, boxes, robot, 1)
            case "^":
                robot = move(walls, boxes, robot, -1j)
            case "<":
                robot = move(walls, boxes, robot, -1)
            case "v":
                robot = move(walls, boxes, robot, 1j)


print(calculate_gps(boxes))
