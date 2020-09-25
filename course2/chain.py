class Event:
    def __init__(self, kind):
        self.kind = kind


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            self.__successor.handle(obj, event)

