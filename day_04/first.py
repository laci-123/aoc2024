from sys import stdin


def find_xmas(grid, start, step):
    return grid.get(start + 1*step) == "M" and grid.get(start + 2*step) == "A" and grid.get(start + 3*step) == "S"
    

grid = {}
rows = 0
cols = 0


for y, line in enumerate(stdin):
    rows += 1
    if cols == 0:
        cols = len(line.strip())
    for x, char in enumerate(line.strip()):
        grid[x + y * 1j] = char


result = 0
for y in range(rows):
    for x in range(cols):
        c = x + y * 1j
        if grid.get(c) == "X":
            for step in [0+1j, 1+1j, 1+0j, 1-1j, 0-1j, -1-1j, -1+0j, -1+1j]:
                if find_xmas(grid, c, step):
                    result += 1


print(result)
