from typing import List, Any, Optional




class QueueList:
    """
    Queue implementation using list in Python. Implements the
    FIFO (First In, First Out) principle.

    >>> queue = QueueList([1, 2, 3, 4])
    >>> queue.get()
    1
    >>> queue.items
    [2, 3, 4]
    >>> queue.get_front()
    2
    """

    def __init__(self, iterable: Optional[Any] = None) -> None:
        # Optional type notation is used to 
        # Indicate that a value can be of a specific type or None.  
        self.items: List[Any] = list(iterable or []) 
        # If None, create the list else, inclement the iterable the user





    def put(self, item: Any) -> None:
        """Sed for adds items in queue"""
        self.items.append(item)




    def get(self) -> Optional[Any]:
        """Used for get the item of the queue and remove"""
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("List in empty")
            return None




    def get_front(self) -> Optional[Any]:
        """Used to only show the fist item"""
        if not self.is_empty():
            return self.items[0]
        else:
            print("List in empty")
            return None





    def is_empty(self) -> bool:
        """Returns True if the queue is empty, False otherwise"""
        return not bool(self.items)




    def size(self) -> int: 
        """Returns the number of items in the queue"""
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
