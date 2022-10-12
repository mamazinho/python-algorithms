def is_str(value):
    if not isinstance(value, str):
        raise TypeError("valor não é str")

class ValidateAttr:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validator(value)
        setattr(obj, self.private_name, value)

class Music:
    title = ValidateAttr(is_str)

    def __init__(self, title):
        self.title = title
