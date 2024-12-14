from sys import stdin
import re


WIDTH = 101
HEIGHT = 103
ITERATIONS = 100

class Robot:
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        

robots = []
for line in stdin:
    px, py, vx, vy = [int(x) for x in re.split("=|,| ", line) if x != "p" and x != "v"]
    robots.append(Robot(px, py, vx, vy))


for i in range(ITERATIONS):
    for robot in robots:
        robot.px = (robot.px + robot.vx) % WIDTH
        robot.py = (robot.py + robot.vy) % HEIGHT


q1 = 0
q2 = 0
q3 = 0
q4 = 0
for y in range(HEIGHT):
    for x in range(WIDTH):
        for robot in robots:
            if robot.px == x and robot.py == y:
                if y < HEIGHT // 2:
                    if x < WIDTH // 2:
                        q1 += 1
                    elif x > WIDTH // 2:
                        q2 += 1
                elif y > HEIGHT // 2:
                    if x < WIDTH // 2:
                        q3 += 1
                    elif x > WIDTH // 2:
                        q4 += 1
                

print(q1 * q2 * q3 * q4)
