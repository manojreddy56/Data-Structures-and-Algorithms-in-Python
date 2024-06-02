class _Node:
    __slots__ = '_element', '_next'
    
    def __init__(self, element, next):
        self._element = element
        self._next = next
        
        
class Linkedlist:
    def __init__(self):
        self._head = None
        self._tail = None   
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0  
    
    def Add_last(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        
    def Add_first(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1
        
    def Add_any(self, e, position):
        newest = _Node(e, None)
        p = self._head
        i = 1
        while i < position-1:
            p = p._next
            i += 1
        newest._next = p._next
        p._next = newest
        self._size += 1
        
    def display(self):
        p = self._head
        while p:
            print(p._element, end="  ")
            p = p._next
        print()
    
    def search(self, key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            else:
                p = p._next
                index += 1
        else:
            return "Element not found"
            
            
L = Linkedlist()
L.Add_last(7)
L.Add_last(4)
L.Add_last(12)
L.display()
print("size: ", len(L))
L.Add_last(8)
L.Add_last(3)
print("size: ", len(L))
print(L.search(8))
print(L.search(10))
L.Add_first(6)
L.display()
L.Add_any(23, 3)
L.display()