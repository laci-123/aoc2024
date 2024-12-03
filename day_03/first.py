from sys import stdin


state = None
x = ""
y = ""
sum = 0

for c in stdin.read():
    match state:
        case None:
            if c == "m":
                state = "m"
            else:
                state = None
        case "m":
            if c == "u":
                state = "u"
            else:
                state = None
        case "u":
            if c == "l":
                state = "l"
            else:
                state = None
        case "l":
            if c == "(":
                state = "("
            else:
                state = None
        case "(":
            if c.isdigit():
                x += c
            elif c == ",":
                x = int(x)
                state = ","
            else:
                x = ""
                y = ""
                state = None
        case ",":
            if c.isdigit():
                y += c
            elif c == ")":
                y = int(y)
                state = ")"
            else:
                x = ""
                y = ""
                state = None
        case ")":
            sum += x * y
            x = ""
            y = ""
            if c == "m":
                state = "m"
            else:
                state = None
            
print(sum)
