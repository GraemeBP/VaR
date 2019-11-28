class class_name():
    """
    Example how to use:
        class_example = class_name(1,2)
        where 1 and 2 are a and b within the class function respectively.

        class_example.class_function(3)
        this calls the function within a class and adds in the extra c parameter.
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def class_function(self, c):
        return self.a + self.b + c
