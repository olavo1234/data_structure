from node import Node
from typing import Any


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

            raise ValueError("Data not found in the list")

        except Exception as e:
            print(f'Ocorred Exeception in remove data {e}')
            return False



    def display(self) -> None:
        try:

            if self.is_empty():
                raise ValueError("List is empty")

            current = self.head

            while current:

                print(current.data, end=' -> ')
                current = current.next

            print(None)

        except Exception as e:
            print(e)



    def size(self) -> int:
        try:
            count = 0
            current = self.head

            while current:

                count += 1

                current = current.next

            return count

        except Exception as e:
            print(e)
            return 0



    def search(self, data: Any) -> bool:
        try:
            current = self.head
            found = False

            while current and not found:

                if current.data == data:
                    found = True
                else:
                    current = current.next

            return found

        except Exception as e:
            print(e)
            return False




def main():

    try:
        list_l = LinkedList()

        list_l.add(10)
        list_l.add(1)
        list_l.add(120)
        list_l.add(200)
        list_l.add(20)

        list_l.remove(200)

        list_l.display()

        print(f'Size overall of linked list: {list_l.size()}')

        print(list_l.search(1))

    except Exception as e:
        print(f'Ocorred Exeception in teste: {e}')



if __name__ == '__main__':
    main()
