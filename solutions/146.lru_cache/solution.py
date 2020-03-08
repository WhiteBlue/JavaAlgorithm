from typing import Dict


class LinkedNode:
    key: int
    val: int
    next: super
    pre: super

    def __init__(self, key: int, val: int) -> None:
        self.next = None
        self.pre = None
        self.key = key
        self.val = val


class LRUCache:
    capacity: int
    occupy: int
    head: LinkedNode
    last: LinkedNode
    tmp: Dict[int, LinkedNode]

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.occupy = 0
        self.head = None
        self.last = None
        self.tmp = dict()

    def _move(self, node):
        # change last node
        if self.last == node:
            if node.pre:
                self.last = node.pre

        # delete node
        if node.pre:
            node.pre.next = node.next
            if node.next:
                node.next.pre = node.pre

        # change head node
        if self.head and self.head != node:
            self.head.pre = node
            node.next = self.head
            node.pre = None

        self.head = node

    def get(self, key: int) -> int:
        if key in self.tmp:
            node = self.tmp[key]

            self._move(node)

            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.tmp:
            node = self.tmp[key]
            node.val = value
            self._move(node)
            # print_link(self.head)
            return

        node = LinkedNode(key, value)

        if self.last and self.head:
            self.last.next = node
            node.pre = self.last
            self.last = node
        else:
            self.head = node
            self.last = node

        self.occupy += 1
        self.tmp[key] = node

        self._move(node)

        if self.occupy > self.capacity:
            self.tmp.pop(self.last.key)
            self.last = self.last.pre
            self.last.next = None
            self.occupy -= 1
        # print_link(self.head)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def print_link(root: LinkedNode):
    node = root
    pre = None
    while node:
        if pre:
            if node.pre == pre:
                print("<-->", end="")
        print("(" + str(node.key) + "," + str(node.val) + ")", end="")
        pre = node
        node = node.next
    print("")
