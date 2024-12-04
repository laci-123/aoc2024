from sys import stdin


def find_x_mas(grid, start):
    one = (grid.get(start + (1+1j)) == "M" and grid.get(start + (-1-1j)) == "S") or (grid.get(start + (-1-1j)) == "M" and grid.get(start + (1+1j)) == "S")
    two = (grid.get(start + (1-1j)) == "M" and grid.get(start + (-1+1j)) == "S") or (grid.get(start + (-1+1j)) == "M" and grid.get(start + (1-1j)) == "S")
    return one and two
    

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
        if grid.get(c) == "A":
            if find_x_mas(grid, c):
                result += 1


print(result)
