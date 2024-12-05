from sys import stdin


def ordering_is_correct(rules, ordering):
    for i, x in enumerate(ordering):
        for y in ordering[(i+1):]:
            if (y, x) in rules:
                return False
    return True


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
    if ordering_is_correct(rules, page_ordering):
        sum += middle_number(page_ordering)


print(sum)
