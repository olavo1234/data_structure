from typing import Any



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
    # used decorator in metode 
    # to make in getters in setters
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
