from sys import stdin
from functools import cmp_to_key


def compare(rules, x, y):
    if (x, y) in rules:
        return -1
    elif (y, x) in rules:
        return 1
    else:
        return 0


def middle_number(numbers):
    return numbers[int(len(numbers)/2)]


rules_list = []
page_orderings = []

currently_reading = "rules"
for line in stdin:
    match currently_reading:
        case "rules":
            if line.strip() == "":
                currently_reading = "pages"
            else:
                rules_list.append(tuple([int(x.strip()) for x in line.split("|")]))
        case "pages":
            page_orderings.append([int(x.strip()) for x in line.split(",")])

rules = set(rules_list)


sum = 0
for page_ordering in page_orderings:
    correct_ordering = sorted(page_ordering, key=cmp_to_key(lambda x, y: compare(rules, x, y)))
    if correct_ordering != page_ordering:
        sum += middle_number(correct_ordering)


print(sum)
