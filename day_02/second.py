from sys import stdin


def possible_dampenings(levels):
    return [[x for k, x in enumerate(levels) if k != i] for i, _ in enumerate(levels)]


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
    

safe_reports = 0
for line in stdin:
    report = [int(x.strip()) for x in line.split()]
    if any([report_is_safe(dampened_report) for dampened_report in possible_dampenings(report)]):
        safe_reports += 1

print(safe_reports)
