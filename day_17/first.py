from sys import stdin


class Machine:
    def __init__(self):
        self.ip = 0
        self.output = []

        
    def fetch(self):
        if self.ip >= len(self.program):
            return None
        return self.program[self.ip], self.program[self.ip + 1]


    def combo(self, operand):
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.register_a
            case 5:
                return self.register_b
            case 6:
                return self.register_c
            case other:
                raise ValueError("Invalid combo operand: " + other)


    def run_step(self, opcode, operand):
        match opcode:
            case 0: #adv
                self.register_a = self.register_a // (2 ** self.combo(operand))
                self.ip += 2
            case 1: #bxl
                self.register_b = self.register_b ^ operand
                self.ip += 2
            case 2: #bst
                self.register_b = self.combo(operand) % 8
                self.ip += 2
            case 3: #jnz
                if self.register_a != 0:
                    self.ip = operand
                else:
                    self.ip += 2
            case 4: #bxc
                self.register_b = self.register_b ^ self.register_c
                self.ip += 2
            case 5: #out
                self.output.append(self.combo(operand) % 8)
                self.ip += 2
            case 6: #bdv
                self.register_b = self.register_a // (2 ** self.combo(operand))
                self.ip += 2
            case 7: #cdv
                self.register_c = self.register_a // (2 ** self.combo(operand))
                self.ip += 2


    def run(self):
        while (op := self.fetch()) != None:
            opcode, operand = op
            self.run_step(opcode, operand)


    def output_str(self):
        return ",".join([str(x) for x in self.output])


    
machine = Machine()
for i, line in enumerate(stdin):
    if line.strip() == "":
        continue
    value = line.split(":")[1].strip()
    match i:
        case 0:
            machine.register_a = int(value)
        case 1:
            machine.register_b = int(value)
        case 2:
            machine.register_c = int(value)
        case 4:
            machine.program = [int(x) for x in value.split(",")]


machine.run()
print(machine.output_str())
