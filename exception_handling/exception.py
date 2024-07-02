class ExcessiveData(Exception):

    def __init__(self, message, note) -> None:
        super().__init__(message)
        self.note = note
