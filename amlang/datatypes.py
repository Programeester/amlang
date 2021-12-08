class class_:

    def __init__(self, name, base, attrs):
        self._make(name, base, attrs)


    def make(self, name, base, attrs, methods):
        return type(name, base, attrs)