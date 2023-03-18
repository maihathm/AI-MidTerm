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
    def clear(self)->None:
        super().clear()

class Queue(__List):
    def __init__(self) -> None:
        super().__init__()
    
    def enQueue(self, item):
        self._list.append(item)
    
    def deQueue(self):
        return self._list.pop(0)
    
    def peek(self):
        return self._list[0]
    def clear(self)->None:
        super().clear()

class PriorityQueue(Queue):
    def __init__(self, key = None) -> None:
        super().__init__()
        self.__key = key
    
    def enQueue(self, item):
        super().enQueue(item)
        self._list.sort(key = self.__key)
    def clear(self)->None:
        super().clear()
  
    # use for tuple format (key, value)
    ## [key0, key1,....]
    def containInTuple(self, item) -> bool:
        return item in [a for a, b in self._list]
    
    def getPriority(self, key):
        for a, b in self._list:
            if a == key:
                return b
        raise KeyError("Cannot find with this key")
    
    def updatePriority(self, key, value):
        oldValue = self.getPriority(key)
        self._list.remove((key, oldValue))
        self.enQueue((key, value))
