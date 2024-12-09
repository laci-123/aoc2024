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


def find_nth_last_file(disk, n):
    k = len(disk) - 1
    id = -1
    length = -1
    for _ in range(n):
        while disk[k] == -1:
            k -= 1
        id = disk[k]
        length = 0
        if k < 0:
            return None
        while disk[k] == id:
            k -= 1
            length += 1
    return (k + 1, id, length)


def find_first_big_enough_free(disk, target_length):
    length = 0
    k = -1
    for i, id in enumerate(disk):
        if id == -1:
            if k == -1:
                k = i
            length += 1
        elif k != -1:
            if length >= target_length:
                return (k, length)
            else:
                length = 0
                k = -1


def defragment(disk):
    n = 0
    while True:
        match find_nth_last_file(disk, n):
            case k, id, len_file:
                i, len_free     = find_first_big_enough_free(disk, len_file)
                if i < k and len_file <= len_free:
                    disk[i:(i + len_file)] = [id] * len_file
                    disk[k:(k + len_file)] = [-1] * len_file
                n += 1
            case _:
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
            continue
        sum += i * x
    return sum
            


line = [int(x) for x in stdin.read().strip()]
disk = decompress(line)
defragment(disk)
print(checksum(disk))
