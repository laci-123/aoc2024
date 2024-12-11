from sys import stdin


class Stone:
    def __init__(self, number, next):
        self.number = number
        self.next = next


def rule_one(stone):
    if stone.number == 0:
        stone.number = 1
        return (True, stone.next)
    return (False, None)


def rule_two(stone):
    digits = str(stone.number)
    if len(digits) % 2 == 0:
        stone.number = int(digits[:(len(digits)//2)])
        new_stone = Stone(int(digits[(len(digits)//2):]), stone.next)
        stone.next = new_stone
        return (True, new_stone.next)
    return (False, None)


def rule_three(stone):
    stone.number *= 2024
    return (True, stone.next)


def apply_rules(stone):
    ok, next_stone = rule_one(stone)
    if ok:
        return next_stone
    ok, next_stone = rule_two(stone)
    if ok:
        return next_stone
    ok, next_stone = rule_three(stone)
    if ok:
        return next_stone


stones = None
for x in reversed(stdin.read().strip().split()):
    stones = Stone(int(x), stones)


first_stone = stones
for _ in range(25):
    stone = first_stone
    while stone:
        stone = apply_rules(stone)


length = 0
stone = first_stone
while stone:
    length += 1
    stone = stone.next


print(length)
