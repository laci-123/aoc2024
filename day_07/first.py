from sys import stdin


def check_equation_imp(result, numbers, acc, operator):
    if len(numbers) == 0:
        return False

    match operator:
        case "+":
            acc += numbers[0]
        case "*":
            acc *= numbers[0]

    if acc == result:
        return True
    elif acc > result:
        return False
    else:
        return check_equation_imp(result, numbers[1:], acc, "+") or check_equation_imp(result, numbers[1:], acc, "*")


def check_equation(result, numbers):
    return check_equation_imp(result, numbers, 0, "+") or check_equation_imp(result, numbers, 1, "*")


sum = 0
for line in stdin:
    result_str, rest = line.split(":")
    result = int(result_str)
    numbers = [int(x) for x in rest.strip().split(" ")]
    if check_equation(result, numbers):
        sum += result


print(sum)
