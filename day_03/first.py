from sys import stdin


transitions = {
    "start": "m",
    "m":     "u",
    "u":     "l",
    "l":     "(",
    "(":     "x",
    "x":     "x",
    ",":     "y",
    "y":     "y",
    ")":     "mul",
}

state = "start"
x = ""
y = ""
sum = 0

for c in stdin.read():
    state = transitions[state]
    match state:
        case "x":
            if c.isdigit():
                x += c
            elif c == ",":
                x = int(x)
                state = ","
            else:
                x = ""
                y = ""
                state = "start"
        case "y":
            if c.isdigit():
                y += c
            elif c == ")":
                y = int(y)
                state = ")"
            else:
                x = ""
                y = ""
                state = "start"
        case "mul":
            sum += x * y
            x = ""
            y = ""
            if c == "m":
                state = "m"
            else:
                state = "start"
        case _:
            if c != state:
                state = "start"
    
            
print(sum)
