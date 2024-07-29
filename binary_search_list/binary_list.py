from typing import Any, List





class BinarySearchList:
    """
    Binary search is an algorithm that divides and 
    searches data according to the size of the element,
    avoiding going through each item in the structure
    """
    
    def __init__(self) -> None:
        self.lst: List[Any] = []



    def is_empty(self) -> bool:
        return len(self.lst) == 0



    def add(self, new_value: Any) -> None:
        
        # Finds the correct position to insert a new item
        index = 0

        while index < len(self.lst) and self.lst[index] < new_value:
            # As long as the corresponding value in the index is less than the new
            # will keep adding until find the dead end
            index += 1
        
        self.lst.insert(index, new_value)



    def remove(self, value: Any) -> Any:
        
        if self.is_empty():
            print('Value Not Found')
            return None

        try:
            self.lst.remove(value)
            return value
        
        except ValueError:
            print('This value cannot be removed.')
            return None



    def search_bin(self, value: Any) -> bool:
    
        if self.is_empty():
            print('The List is empty')
            return None

        bottom = 0
        higher = len(self.lst) - 1 

        # Stop loop only when higher pointer 
        # smaller that the bottom pointer

        while bottom <= higher:

            center = (bottom + higher) // 2
            
            if self.lst[center] == value:
                # Compares whether the pointer 
                # value si equal to the center
                
                return True
            
            elif self.lst[center] < value:
                # If elementer of center is smaller value
                bottom = center + 1 # adds the index of all ignored elements
                # Adds the value of the pointer center
                # The entire left part of the list ignored 
            else:
                higher = center - 1

        return False



    def display(self) -> None:

        if self.is_empty():
            print('The List is empty')
        
        for _ in self.lst:
            print(_)



def main():

    lst_search = BinarySearchList()

    lst_search.add(100)
    lst_search.add(1000)
    lst_search.add(4)
    lst_search.add(1)
    lst_search.add(5)
    lst_search.add(50)
    lst_search.add(30)
    lst_search.add(20)

    lst_search.display()

    print(lst_search.search_bin(10))



if __name__ == "__main__":
    main()
