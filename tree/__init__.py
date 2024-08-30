from typing import Optional





"""
Trees are an abstract data structure that represents hierarchies and relationships between elements. 
It is composed of nodes connected by edges. Just like a linked list, 
a tree contains pointers that store addresses for subtrees called "left" and "right", 
a binary tree will always have a node with the reference of these 2 pointers. Several metaphors are 
composed in this data structure, following the metaphor of a "tree", the first node is called the root, 
the subsequent nodes are layers of branches and the tip node is called leaves. Another metaphor is the family tree,
where the main one is called "father" and the nodes that refer to it are called "son", 
nodes with the same father are called "siblings". And the last one is geometric vocabulary, 
as already mentioned "left" and "right" and there are also
"up" (in the direction of the root) and "down" (in the direction of the leaves).
"""




class Node:
    """ 
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))

    print_tree(tree)

    #         -> 7
    #     -> 3
    #         -> 6
    # -> 1
    #         -> 5
    #     -> 2
    #         -> 4
    """
    
    def __init__(self, key: int, left: Optional['Node'] = None, right: Optional['Node'] = None) -> None:
        self.key = key 
        self.left = left
        self.right = right



    def __str__(self) -> str:
        return str(self.value)




def print_tree(node: Node, level=0) -> None:
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.key)
        print_tree(node.left, level + 1)
