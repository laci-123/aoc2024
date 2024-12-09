from sys import stdin


class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        p = self.next
        n = Node(value, self, self.next)
        self.next = n
        if p != None:
            p.prev = n
        return n

    def delete_next(self):
        if self.next:
            p = self.next.next
            self.next = p
            if p:
                p.prev = self


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def append(self, value):
        if self.last:
            self.last = self.last.insert_after(value)
        else:
            self.first = Node(value, None, None)
            self.last = self.first


class Block:
    def __init__(self, id, length):
        self.id = id
        self.length = length


def decompress(disk):
    is_file = True
    id = 0
    result = LinkedList()
    for x in disk:
        if is_file:
            result.append(Block(id, x))
            id += 1
        else:
            result.append(Block(-1, x))
        is_file = not is_file
    return result


def defragment(disk):
    file = disk.last
    while file:
        if file.value.id == -1:
            file = file.prev
        free = disk.first
        ids = []
        while free:
            ids.append(free.value.id)
            while free.value.id != -1:
                free = free.next
                ids.append(free.value.id)
            if file.value.length <= free.value.length and file.value.id not in ids:
                rem_length = free.value.length - file.value.length
                free.value.id = file.value.id
                free.value.length = file.value.length
                if rem_length > 0:
                    free.insert_after(Block(-1, rem_length))
                file.value.id = -1
                if file.next and file.next.value.id == -1:
                    file.value.length += file.next.value.length
                    file.delete_next()
                if file.prev and file.prev.value.id == -1:
                    file.prev.value.length += file.value.length
                    file.prev.delete_next()
                break
            free = free.next
        file = file.prev


def pretty_print(disk):
    s = ""
    node = disk.first
    while node:
        if node.value.id == -1:
            s += "." * node.value.length
        else:
            s += str(node.value.id) * node.value.length
        node = node.next
    return s


def checksum(disk):
    sum = 0
    node = disk.first
    i = 0
    while node:
        if node.value.id != -1:
            for _ in range(node.value.length):
                sum += i * node.value.id 
                i += 1
        else:
            i += node.value.length
        node = node.next
    return sum
            


line = [int(x) for x in stdin.read().strip()]
disk = decompress(line)
# print(pretty_print(disk))
defragment(disk)
# print(pretty_print(disk))
print(checksum(disk))
