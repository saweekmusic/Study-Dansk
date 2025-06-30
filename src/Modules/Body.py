class Body:
    def __init__(self) -> None:
        pass

    def render(self):
        raise NotImplementedError("Subclasses should implement this method")
    
class WordContent(Body):
    pass

class TableContent(Body):
    pass

class TextContent(Body):
    pass