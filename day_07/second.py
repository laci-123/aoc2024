from sys import stdin


def number_of_digits(x):
    digits = 0
    while x >= 1:
        x = x // 10
        digits += 1
    return digits


def check_equation_imp(result, numbers, acc, operator):
    if len(numbers) == 0:
        return False

    match operator:
        case "+":
            acc += numbers[0]
        case "*":
            acc *= numbers[0]
        case "|":
            x = numbers[0]
            e = number_of_digits(x)
            acc = (10 ** e) * acc + x

    if acc > result:
        return False
    elif acc == result and len(numbers) == 1:
        return True
    else:
        return check_equation_imp(result, numbers[1:], acc, "+") or check_equation_imp(result, numbers[1:], acc, "*") or check_equation_imp(result, numbers[1:], acc, "|")


def check_equation(result, numbers):
    return check_equation_imp(result, numbers, 0, "+") or check_equation_imp(result, numbers, 1, "*") or check_equation_imp(result, numbers[1:], 0, "|")


sum = 0
for line in stdin:
    result_str, rest = line.split(":")
    result = int(result_str)
    numbers = [int(x) for x in rest.strip().split(" ")]
    if check_equation(result, numbers):
        sum += result


print(sum)

