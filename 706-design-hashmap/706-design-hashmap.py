class EmptyValue:
    """ For storing empty value """
    pass    


class LLNode:
    """ Node of linked list """

    def __init__(self, key: int, val: int, next: Optional['LLNode'] = None) -> None:
        self.key = key
        self.val = val
        self.next = next
class MyHashMap:

    def __init__(self):
        self.empty = EmptyValue()
        self.size = 2069
        self.data = [self.empty] * self.size
        
    def _get_index(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._get_index(key)
        if self.data[index] is self.empty:
            self.data[index] = LLNode(key, value)
        else:
            node = self.data[index]
            while node:
                if node.key == key:
                    node.val = value
                    return
                node = node.next
            self.data[index] = LLNode(key, value, self.data[index])

    def get(self, key: int) -> int:
        index = self._get_index(key)
        if self.data[index] is not self.empty:
            node = self.data[index]
            while node:
                if node.key == key:
                    return node.val
                node = node.next
        return -1

    def remove(self, key: int) -> None:
        index = self._get_index(key)
        if self.data[index] is not self.empty:
            prev = None
            node = self.data[index]
            while node:
                if node.key == key:
                    if prev:
                        prev.next = node.next
                    else:
                        self.data[index] = node.next or self.empty
                    return
                prev = node
                node = node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)