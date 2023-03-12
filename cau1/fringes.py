class Stack:
    def __init__(self) -> None:
        self.__stk = []
    
    def size(self) -> int:
        return len(self.__stk)
    
    def empty(self) -> bool:
        return self.size() == 0
    
    def push(self, item):
        self.__stk.append(item)
    
    def pop(self):
        if len(self.__stk) > 0:
            return self.__stk.pop()
        else:
            return None
    
    def peek(self):
        if len(self.__stk) > 0:
            return self.__stk[-1]
        else:
            return None
    
    def __str__(self) -> str:
        return str(self.__stk)

class Queue:
    def __init__(self) -> None:
        self.__qu = []
    
    def size(self) -> int:
        return len(self.__qu)
    
    def empty(self) -> bool:
        return self.size() == 0
    
    def enQueue(self, item):
        self.__qu.append(item)
    
    def deQueue(self):
        if len(self.__qu) > 0:
            return self.__qu.pop(0)
        else:
            return None
    
    def peek(self):
        if len(self.__qu) > 0:
            return self.__qu[0]
        else:
            return None
    
    def __str__(self) -> str:
        return str(self.__qu)

class PriorityQueue:
    def __init__(self, key = None) -> None:
        self.__heap = []
        self.__key = key
    
    def size(self) -> int:
        return len(self.__heap)
    
    def empty(self) -> bool:
        return self.size() == 0
    
    def enQueue(self, item):
        self.__heap.append(item)
        self.__heap.sort(key = self.__key)
    
    def deQueue(self):
        self.__heap.pop(0)
    
    def peek(self):
        if len(self.__heap) > 0:
            return self.__heap[0]
        else:
            return None
    
    def __str__(self) -> str:
        return str(self.__heap)