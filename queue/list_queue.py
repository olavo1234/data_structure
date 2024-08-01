from typing import List, Any




class QueueList:
    """
    Queue implementation by list in python. Use 
    the concept FIFO(Fist in, Fist out) to add and remove elements.

    >>> queue = QueueList([1,2,3,4])
    >>> print(queue.get())
    >>> 1
    >>> print(queue.items)
    >>> [2,3,4]
    >>> print(queue.get_front())
    >>> 2
    
    """

    def __init__(self, iterable: Any | None = None) -> None:
        self.items: List[Any] = list(iterable or [])




    def put(self, item: Any) -> None:
        """Sed for adds items in queue"""
        self.items.append(item)




    def get(self) -> Any:
        """Used for get the item of the queue and remove"""
        try:    
            if not self.is_empty():
                return self.items.pop(0)
            raise IndexError
        except Exception:
            print(f'List is empty')




    def get_front(self):
        """Used to only show the fist item"""
        try:
            return self.items[0]
        except IndexError:
            print("List is empty")




    def is_empty(self):
        return not self.items




    def size(self): 
        return len(self.items)




    def __repr__(self) -> str:
        return str(self.items)




def main():

    queue = QueueList([])

    print(queue.items)

    print(queue.get())

    print(queue.items)

    print(queue.get_front())

    print(queue.is_empty())

    print(queue.size())



if __name__ == "__main__":
    main()
