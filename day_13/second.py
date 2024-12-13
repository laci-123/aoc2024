from sys import stdin
import math


A_TOKEN = 3
B_TOKEN = 1
MAX_PRESSES = 100
CORRECTION = 10000000000000


class Machine:
    def __init__(self):
        self.button_a_x = -1
        self.button_a_y = -1
        self.button_b_x = -1
        self.button_b_y = -1
        self.prize_x = -1
        self.prize_y = -1


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
        machine.prize_x = x + CORRECTION
        machine.prize_y = y + CORRECTION
        machines.append(machine)
        machine = Machine()
        
# For each machine we need to solve a system of linear equations with two unknowns and two equations:
#
# a * button_a_x + b * button_b_x = prize_x
# a * button_a_y + b * button_b_y = prize_y
#
# where a and b must be positive integers.

prize = 0
for machine in machines:
    p = machine.prize_y * machine.button_b_x - machine.prize_x * machine.button_b_y
    q = machine.button_a_y * machine.button_b_x - machine.button_a_x * machine.button_b_y
    if p % q == 0:
        a = p // q
        r = machine.prize_x - a * machine.button_a_x 
        if r % machine.button_b_x == 0:
            b = r // machine.button_b_x
            prize += a * A_TOKEN + b * B_TOKEN


print(prize)
