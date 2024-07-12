class ExcepMaster(Exception):
    """Class base for other exceptions"""
    
    pass



class NodeNotFoundError(ExcepMaster):
    """Exeception for nodes not found"""

    def __init__(self, message='Node not Found in the operation.') -> None:
        self.message = message
        super().__init__(self.message)





