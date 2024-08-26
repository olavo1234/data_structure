from typing import Any





class NodeNotFoundError(Exception):

    def __init__(self, message='Node not Found in the operation.') -> None:
        self.message = message
        super().__init__(self.message)




class Node:

    def __init__(self, data: Any) -> None:
        self.__data = data
        self.__prev = None
        self.__next = None



    @property
    def data(self) -> Any:
        return self.__data



    @property
    def next(self) -> Any:
        return self.__next



    @property
    def prev(self) -> Any:
        return self.__prev



    @prev.setter
    def prev(self, new_prev: Any) -> None:
        self.__prev = new_prev



    @data.setter
    def data(self, new_data: Any) -> None:
        self.__data = new_data



    @next.setter
    def next(self, new_next: Any) -> None:
        self.__next = new_next




class DoublyLinkedList:
    """
    This structure is similar to the singly 
    linked list, however, with an extra 
    pointer pointing to the previous node.

    head node[1] <--> node[2] <--> node[3] <--> none
    #     (0x01)      (0x02)       (0x03)
    """

    def __init__(self) -> None:
        self.head = None



    def add_start_list(self, data: Any) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node



    def add_end_list(self, data: Any) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
        # Add the previous at current
        new_node.prev = current



    def remove(self, data: Any) -> bool:
        """
        o metodo de remover tem que ser implementado 
        sempre tomando o cuidado para não quebrar a itegridade da 
        estrutura, reajustando o ponteiro 'next' e o 'prev'.
        """
        current = self.head

        while current:
            if current.data == data:
                # Readjustment of pointers to maintain list structure
                if current.prev:
                    # Define next of previous to next current
                    current.prev.next = current.next
                if current.next:
                    # Define previous of next to current previous
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next

                return True

            current = current.next
            
        raise NodeNotFoundError



    def display(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next



    def display_reverse(self):
        """
        This method was the list in reverse order, 
        first up to the last node and then, 
        iterating and displaying in the prev pointer.
        """
        current = self.head

        while current and current.next:
            current = current.next
        
        while current:
            print(current.data)
            current = current.prev



    def insert_at_position(self, data: Any, position: int=0):
        """
        This method consists of inserting a new node in
        a position in the list, if it exceeds the position, 
        the node will be added at the end.
        """
        new_node = Node(data)

        if position == 0:
            # If the position to 0, add in the start 
            self.add_start_list(data)
            return

        elif self.head is None:
            # If the list is empty, add the new node as the first node
            self.head = new_node
            return
        
        current = self.head
        current_position = 0 

        # Advance to the position or to end list
        while current_position < position - 1 and current.next:
            current = current.next
            current_position += 1

        if current_position == position - 1:
            new_node.next = current.next
            new_node.prev = current
        
            if current.next: # if not inserted at the end of the lis
                current.next.prev = new_node
        
            current.next = new_node
        else:
            # If position is greater than list size, add at the end
            current.next = new_node
            new_node.prev = current




def main():
    
    lt = DoublyLinkedList()

    lt.add_end_list(10)
    lt.add_end_list(12)
    lt.add_end_list(1)
    print("----------------")
    lt.insert_at_position(5)
    print("----------------")
    
    lt.display()
    print("----------------")
    lt.display_reverse()



if __name__ == "__main__":
    main()
