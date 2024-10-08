from typing import Any





class Node:

    def __init__(self, data: Any) -> None:
        self.__data = data
        self.__next = None



    @property
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




class Binary_Linked_List:
    """
    Binary search inplamentation in linked list.
    
    >>> binary_linked_list = Binary_Linked_List()
    >>> print(binary_linked_list.search_bin(11))
    False
    >>> binary_linked_list.add(10)
    >>> print(binary_linked_list.search_bin(10))
    True
    """

    def __init__(self) -> None:
        self.head = None



    def display(self) -> None:
        current = self.head

        while current:

            print(current.data)

            current = current.next
        
        print(None)



    def add_start_list(self, data: Any) -> None:
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node



    def add_end_list(self, new_data: Any) -> None:
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            
            return new_data
        
        current = self.head

        while current.next:
            
            current = current.next
        
        current.next = new_node

        return new_data



    def remove(self, data: Any) -> None:
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

        return False



    def form_list(self) -> list:
        """Method of adding nodes to a list in ascending order."""
        lst = list()
        current = self.head

        index = 0

        while current:

            while index < len(lst) and lst[index] < current.data:
                # This compare lenght the list and value the node
                index += 1
            
            # Insertion the node in list 
            lst.insert(index, current.data)
            
            current = current.next
        
        return lst



    def search_bin(self, value: Any) -> bool:
        lst = self.form_list()
        # The function is called for create is list 
        # The list must be organized for searching

        bottom = 0
        higher = len(lst) - 1

        while bottom <= higher:

            center = (bottom + higher) // 2

            if lst[center] == value:
                
                return True
            
            elif lst[center] < value:
                bottom = center + 1
            else:
                higher = center - 1
        
        return False




def main():

    binary_linked_list = Binary_Linked_List()

    binary_linked_list.add(10)
    binary_linked_list.add(1)
    binary_linked_list.add(110)
    binary_linked_list.add(11)
    binary_linked_list.add(40)
    binary_linked_list.add(200)
    binary_linked_list.add(200)

    binary_linked_list.remove(200)

    binary_linked_list.display()

    print(binary_linked_list.search_bin(11))



if __name__ == "__main__":
    main()
