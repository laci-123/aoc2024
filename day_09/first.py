from sys import stdin


def decompress(disk):
    is_file = True
    id = 0
    result = []
    for x in disk:
        if is_file:
            result += [id] * x
            id += 1
        else:
            result += [-1] * x
        is_file = not is_file
    return result


def defragment(disk):
    length = len(disk)
    k = length -1
    for i in range(length):
        if disk[i] == -1:
            while disk[k] == -1:
                k -= 1
            disk[i] = disk[k]
            disk[k] = -1
            k -= 1
        if k == i:
            break


# def pretty_print(disk):
#     s = ""
#     for x in disk:
#         if x == -1:
#             s += "."
#         else:
#             s += str(x)
#     return s


def checksum(disk):
    sum = 0
    for i, x in enumerate(disk):
        if x == -1:
            break
        sum += i * x
    return sum
            


line = [int(x) for x in stdin.read().strip()]
disk = decompress(line)
defragment(disk)
print(checksum(disk))
