from node import Node
from typing import Any
from linked_list.exception_node import NodeNotFoundError



class LinkedList:
    """
    Linked list is a structure that handles nodes,
    forming a line with head and methods for append, remove.
    """

    def __init__(self) -> None:
        self.head = None



    def is_empty(self):
        return self.head is None



    def add(self, data: Any) -> None:
        
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head

        while current.next:

            current = current.next

        current.next = new_node



    def remove(self, data: Any) -> bool:
        try:
            current = self.head
            prev = None

            while current:
                if current.data == data:
                    if prev:
                        prev.next = current.next
                    else:
                        self.head = current.next

                    return True

                prev = current 

                current = current.next

            raise NodeNotFoundError

        except NodeNotFoundError as e:
            print(f'Ocorred Exeception in remove data. {e}')
            return False



    def display(self) -> None:

        if self.is_empty():
            print('List is empty')

        current = self.head

        while current:

            print(current.data, end=' -> ')
            current = current.next

        print(None)



    def size(self) -> int:

        count = 0
        current = self.head

        while current:

            count += 1

            current = current.next

        return count



    def search(self, data: Any) -> bool:

        current = self.head
        found = False

        while current and not found:

            if current.data == data:
                found = True
            else:
                current = current.next

        return found



def main():

    try:
        list_l = LinkedList()

        list_l.add(1)
        list_l.add(120)
        list_l.add(200)
        list_l.add(20)

        list_l.remove(200)

        list_l.display()

        print(f'Size overall of linked list: {list_l.size()}')

        print(list_l.search(1))

        list_l.remove(10)

    except Exception as e:
        print(f'Ocorred Exeception in teste: {e}')




if __name__ == '__main__':
    main()
