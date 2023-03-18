class __List:
    def __init__(self) -> None:
        self._list = []

    def size(self) -> int:
        return len(self._list)

    def empty(self) -> bool:
        return len(self._list) == 0

    def contain(self, item) -> bool:
        return item in self._list

    def clear(self)->None:
        self._list.clear()

    def __str__(self) -> str:
        return str(self._list)

class Stack(__List):
    def __init__(self) -> None:
        super().__init__()

    def push(self, item):
        self._list.append(item)

    def pop(self):
        return self._list.pop()

    def peek(self):
        return self._list[-1]

class Queue(__List):
    def __init__(self) -> None:
        super().__init__()
    
    def enQueue(self, item):
        self._list.append(item)
    
    def deQueue(self):
        return self._list.pop(0)
    
    def peek(self):
        return self._list[0]

class PriorityQueue(Queue):
    def __init__(self, key = None) -> None:
        super().__init__()
        self.__key = key

    def enQueue(self, item):
        super().enQueue(item)
        self._list.sort(key = self.__key)
