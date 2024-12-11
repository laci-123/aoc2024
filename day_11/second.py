from sys import stdin
import functools


def apply_rules(number):
    if number == 0:
        return 1
    digits = str(number)
    if len(digits) % 2 == 0:
        return (int(digits[:(len(digits)//2)]), int(digits[(len(digits)//2):]))
    return number * 2024


@functools.cache
def find_length(number, blink):
    if blink == 0:
        return 1
    
    match apply_rules(number):
        case (x, y):
            return find_length(x, blink - 1) + find_length(y, blink - 1)
        case x:
            return find_length(x, blink - 1)


stones = [int(x) for x in stdin.read().strip().split()]


length = 0
for stone in stones:
    length += find_length(stone, 75)


print(length)
