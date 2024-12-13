from sys import stdin


A_TOKEN = 3
B_TOKEN = 1
MAX_PRESSES = 100


class Machine:
    def __init__(self):
        self.button_a_x = -1
        self.button_a_y = -1
        self.button_b_x = -1
        self.button_b_y = -1
        self.prize_x = -1
        self.prize_y = -1

    def __str__(self):
        return f"({self.button_a_x}, {self.button_a_y}, {self.button_b_x}, {self.button_b_y}, {self.prize_x}, {self.prize_y})"


machines = []
machine = Machine()
for i, line in enumerate(stdin):
    if i % 4 == 3:
        continue
    x = int(line[(line.find("X") + 2):line.find(",")])
    y = int(line[(line.find("Y") + 2):])
    if i % 4 == 0:
        machine.button_a_x = x
        machine.button_a_y = y
    elif i % 4 == 1:
        machine.button_b_x = x
        machine.button_b_y = y
    elif i % 4 == 2:
        machine.prize_x = x
        machine.prize_y = y
        machines.append(machine)
        machine = Machine()
        

prize = 0
for machine in machines:
    for a in range(MAX_PRESSES + 1):
        for b in range(MAX_PRESSES + 1):
            ax = a * machine.button_a_x
            bx = b * machine.button_b_x
            ay = a * machine.button_a_y
            by = b * machine.button_b_y
            if ax + bx == machine.prize_x and ay + by == machine.prize_y:
                prize += a * A_TOKEN + b * B_TOKEN


print(prize)
