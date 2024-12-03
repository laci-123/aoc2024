from sys import stdin


def parse_any(string):
    if len(string) > 0:
        return (string[0], string[1:])
    else:
        return (False, string)
    

def parse_literal(literal, string):
    if string.startswith(literal):
        return (True, string[len(literal):])
    else:
        return (False, string)


def parse_int(string):
    i = 1
    s = ""
    while i < len(string) and string[:i].isdigit():
        s += string[i - 1]
        i += 1
    if len(s) > 0:
        return (int(s), string[(i-1):])
    else:
        return (False, string)
                

def parse_mul(string):
    (ok, rest) = parse_literal("mul(", string)
    if not ok:
        return (False, string)

    (x, rest) = parse_int(rest)
    if not x:
        return (False, string)
    
    (ok, rest) = parse_literal(",", rest)
    if not ok:
        return (False, string)

    (y, rest) = parse_int(rest)
    if not y:
        return (False, string)

    (ok, rest) = parse_literal(")", rest)
    if not ok:
        return (False, string)
    
    return (x * y, rest)


def parse_sum(string):
    sum = 0
    rest = string
    enabled = True
    while True:
        (p, rest) = parse_mul(rest)
        if p:
            if enabled:
                sum += p
            continue
        (do, rest) = parse_literal("do()", rest)
        if do:
            enabled = True
            continue
        (dont, rest) = parse_literal("don't()", rest)
        if dont:
            enabled = False
            continue
        (ok, rest) = parse_any(rest)
        if not ok:
            return (sum, "")
        

(sum, _) = parse_sum(stdin.read())
print(sum)
