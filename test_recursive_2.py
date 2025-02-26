from __future__ import annotations

from abc import ABC, abstractmethod
from random import randint


class Controller:
    def __init__(self):
        self.tasks_database_ids = {}

    def recursive_dependencies(self, lookup_task):        
        main_dependencies = []
        for dependency in lookup_task.dependencies:
            self.recursive_dependencies(dependency)
            task_instance = Task.get_instance("odin_123", dependency)
            main_dependencies.append(task_instance.get_database_id("odin_123"))

        task_instance = Task.get_instance("odin_123", lookup_task)
        if not task_instance.should_run():
            return
        if task_instance.get_database_id("odin_123"):
            return
        task_instance.save_database_id(randint(1, 1000), "odin_123")


class Task(ABC):
    task_type: str
    dependencies: list | None = None
    _database_ids = {}
    _instances = {}

    def __new__(cls, odin: str):
        instance = super().__new__(cls)
        instance_key = cls.build_instance_key(odin, cls.__name__)
        cls._instances[instance_key] = instance
        return instance
    
    @classmethod
    def get_instance(cls, odin, task_class):
        if isinstance(task_class, Task):
            return task_class 
        instance_key = cls.build_instance_key(odin, task_class.__name__)
        return cls._instances[instance_key]

    @staticmethod
    def build_instance_key(odin: str, task_class_name: str):
        return f"{odin}-{task_class_name}"

    @abstractmethod
    def should_run(self) -> bool:
        ...

    def get_database_id(self, odin: str):
        instance_key = Task.build_instance_key(odin, self.__class__.__name__)
        return self._database_ids.get(instance_key, None)

    def save_database_id(self, id: str, odin: str):
        instance_key = Task.build_instance_key(odin, self.__class__.__name__)
        self._database_ids[instance_key] = id

class A(Task):
    task_type = "EU SOU O A"
    dependencies = []

    def should_run(self):
        return True

class B(Task):
    task_type = "EU SOU O B"
    dependencies = [A]

    def should_run(self):
        return True

class C(Task):
    task_type = "EU SOU O C"
    dependencies = [A,B]

    def should_run(self):
        return False

class D(Task):
    task_type = "EU SOU O D"
    dependencies = [C]

    def should_run(self):
        return True

class E(Task):
    task_type = "EU SOU O E"
    dependencies = [D]

    def should_run(self):
        return False

class F(Task):
    task_type = "EU SOU O F"
    dependencies = [B,C,D]

    def should_run(self):
        return False


if __name__ == "__main__":
    c = Controller()
    all_tasks = [A("odin_123"), B("odin_123"), C("odin_123"), D("odin_123")]

    for i, task in enumerate(all_tasks):
        c.recursive_dependencies(task)
    
    for task in all_tasks:
        print(task, task.get_database_id("odin_123"))
