from sys import stdin


def report_is_safe(levels):
    increasing = None
    for (x, y) in zip(levels, levels[1:]):
        step = y - x
        if 1 <= abs(step) <= 3:
            if increasing is None:
                increasing = (0 < step)
            else:
                if increasing != (0 < step):
                    return False
        else:
            return False
    return True
    

safe_levels = 0
for line in stdin:
    levels = [int(x.strip()) for x in line.split()]
    if report_is_safe(levels):
        safe_levels += 1

print(safe_levels)
