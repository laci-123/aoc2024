from sys import stdin
import re
import array


WIDTH = 101
HEIGHT = 103
ITERATIONS = 100


def writePPM(pixels, width, height, filename):
    PPMheader = "P6\n" + str(width) + " " + str(height) + "\n255\n"
    image = array.array("B", pixels)
    with open(filename, "wb") as f:
        f.write(bytearray(PPMheader, "ascii"))
        image.tofile(f)


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


for i in range(10000):
    for robot in robots:
        robot.px = (robot.px + robot.vx) % WIDTH
        robot.py = (robot.py + robot.vy) % HEIGHT

    # When looking at the generated pictures
    # I noticed that starting at the 97th
    # every 101th image has a kind of clustering pattern,
    # so I thought maybe the image we're looking
    # for will also be at a mutliple of 101.
    # I was lucky.
    if (i - 97) % 101 != 0:
        continue

    pixels = []
    for y in range(HEIGHT):
        for x in range(WIDTH):
            found = False
            for robot in robots:
                if robot.px == x and robot.py == y:
                    found = True
                    break
            if found:
                pixels += [255, 255, 255]
            else:
                pixels += [0, 0, 0]

    writePPM(pixels, WIDTH, HEIGHT, f"image_{i}.ppm")
    print(i)
