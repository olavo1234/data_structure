from typing import List, Any





class StackOverFlowError(Exception):
    """Will be thrown if the stack limit is exceeded."""
    pass




class StackUnderFlowError(Exception):
    """Will be thrown if you perform the operation on the empty stack."""
    pass




class Stack:
    """
    Stack uses the concept LIFO (last in, first out) for 
    adding and removing elements. push() Adds elements to the stack,
    pop() removes elements, peek() returns the fist element.

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

    def __init__(self, limit: int = 10) -> None:
        # The limit is pre set in 10
        self.__data: List[Any] = []
        self.__index = 0 
        self.__limit = limit



    def is_empty(self) -> bool:
        return len(self.__data) == 0 



    def push(self, item: Any) -> None:
        """Add an item to the top of the stack."""
        if self.size() >= self.__limit:
            raise StackOverFlowError
        
        self.__data.append(item)



    def pop(self) -> Any:
        """Represent the pop of list no parameter."""
        if self.is_empty():
            raise StackUnderFlowError

        return self.__data.pop()



    def peek(self) -> Any:
        """Returns the fist element in stack."""
        if self.is_empty():
            raise StackUnderFlowError
        
        return self.__data[-1]



    def size(self) -> int:
        return len(self.__data)



    def __repr__(self) -> str:
        """Get the data in string format."""
        return str(self.__data)



    def __iter__(self):
        """Iteration to loop 'for'."""
        self.__index = len(self.__data) - 1 # starts from the last element
        return self



    def __next__(self):
        """Next item for the loop iteration."""
        if self.__index == 0:
            raise StopIteration

        self.__index -= 1
        return self.__data[self.__index]



    def __bool__(self) -> bool:
        """For iteration with the while."""
        # Returns the inverse of the empty method
        return not self.is_empty()




def main():

    stack_lst = Stack()

    stack_lst.push(10)
    stack_lst.push(140)
    stack_lst.push(1)
    stack_lst.push(4)
    stack_lst.push(7)

    for v in stack_lst:
        print(v)

    print(stack_lst.size())
    print(stack_lst.pop())
    print(stack_lst.peek())
    print(stack_lst.is_empty())



if __name__ == '__main__':
    main()
