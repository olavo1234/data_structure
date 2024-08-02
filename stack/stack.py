from typing import List, Any





class StackOverFlowError(Exception):
    pass




class StackUnderFlowError(Exception):
    pass




class Stack:
    """
    The Stack representation in the class. The Stack use the concept 
    LIFO(Last in, First out) to add and remove elements.

    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> stack.push(3)
    >>> print(stack.pop()) 
    3
    >>> print(stack.peek())   
    2 
    >>> print(stack.is_empty()) 
    False
    """

    def __init__(self) -> None:
        # list to save elements
        self.__data: List[Any] = []
        # index for stack
        self.__index = 0    




    def is_empty(self) -> bool:
        return not self.__data




    def append(self, item: Any) ->None:
        """represent the append of lista"""
        self.__data.append(item)




    def pop(self) -> None:
        """represent the pop of list no parameter"""
        if self.is_empty():
            return

        return self.__data.pop()




    def peek(self) -> Any:
        if self.is_empty():
            return
        
        return self.__data[-1]



    def size(self) -> int:
        return len(self.__data)



    def __repr__(self) -> str:
        """Get the data in string format"""
        return str(self.__data)




    def __iter__(self):
        """itaration to loop 'for'"""
        self.__index = len(self.__data)
        return self




    def __next__(self):
        """Next item for the loop iteration"""
        if self.__index == 0:
            raise StopIteration

        self.__index -= 1
        return self.__data[self.__index]




    def __bool__(self):
        """for iteration with the while"""
        return bool(self.__data)




def main():

    stack_lst = Stack()

    stack_lst.append(10)
    stack_lst.append(140)
    stack_lst.append(1)
    stack_lst.append(4)
    stack_lst.append(7)
    stack_lst.append(57)

    for v in stack_lst:
        print(v)
    print(None)

    print(stack_lst.size())
    print(stack_lst.pop())
    print(stack_lst.peek())
    print(stack_lst.is_empty())




if __name__ == '__main__':
    main()
