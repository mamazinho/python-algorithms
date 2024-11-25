class Task:
    task_type: str
    _instances = {}

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls._instances[cls.__name__] = instance
        return instance
    
    @classmethod
    def __class_getitem__(cls, class_name):
        return cls._instances[class_name]


class A(Task):
    def __init__(self, value):
        self.value = value

    def see_values(self):
        print(self.value)


if __name__ == "__main__":
    a = A(10)

    Task["B"].see_values()