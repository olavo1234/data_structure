from typing import Any







class NodeNotFoundError(Exception):
    """Exeception for nodes not found"""

    def __init__(self, message='Node not Found in the operation.') -> None:
        self.message = message
        super().__init__(self.message)




class Node:
    """
    In the linked list, a node is used to store data.
    Each node contains two elements:
    the value and the reference to the next node. 
    """

    def __init__(self, data: Any) -> None:
        self.__data = data
        self.__next = None




    @property
    # Used decorator in metode 
    # To make in getters in setters
    def data(self) -> Any:
        return self.__data




    @property
    def next(self) -> Any:
        return self.__next




    @data.setter
    def data(self, new_data: Any) -> None:
        self.__data = new_data




    @next.setter
    def next(self, new_next: Any) -> None:
        self.__next = new_next




class LinkedList:
    """
    Linked list is a structure that handles nodes,
    forming a line with head and methods for append, remove.
    
    
    # [] -> data   [] Next
    #   value      reference to new value 

    
    # Use of class LinkedList 
    # head -> Node(1) -> Node(2) -> Node(3) -> None
    #          (0x01)    (0x02)    (0x03)
    """

    def __init__(self) -> None:
        self.head = None



    def is_empty(self):
        return self.head is None



    def add(self, data: Any) -> None:
        
        new_node = Node(data)

        if self.head is None:
            # The new node become head
            self.head = new_node
            return
        
        current = self.head
    
        while current.next:
            # Walk the list with while loop
            # The loop stop in node who has the next pointer 

            current = current.next
            # Walk next node 

        current.next = new_node
        # Set to next node in the pointer



    def remove(self, data: Any) -> bool:
        current = self.head
        prev = None
        # Previous is the predecessor to current

        while current:
            if current.data == data:
                if prev:
                    # Will change the next of the previous 
                    # to be the next of the current 
                    prev.next = current.next        
                else:
                    # Case the value is first
                    # the head becomes a next pointer
                    self.head = current.next

                return True

            prev = current 
            # Define the predecessor for current
            current = current.next
            # The pointer current moves to next node

        raise NodeNotFoundError




    def display(self) -> None:

        if self.is_empty():
            print('List is empty')

        current = self.head

        while current:

            print(current.data, end=' -> ')
            # Renew the pointer for next address
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



    def form_list(self) -> list:

        lst = list()
        current = self.head

        while current:

            lst.append(current.data)
            
            current = current.next
        
        return lst




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

        print(f'Minha lista é: {list_l.form_list()}')

    except Exception as e:
        print(f'Ocorred Exeception in teste: {e}')



if __name__ == '__main__':
    main()
