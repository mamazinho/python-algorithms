from __future__ import annotations
from random import randint
from abc import ABC, abstractmethod


class Controller:
    def __init__(self):
        self.tasks_database_ids = {}

    def recursive_dependencies(self, lookup_task):        
        main_dependencies = []
        for dependency in lookup_task.dependencies:
            self.recursive_dependencies(dependency)
            database_id = self.tasks_database_ids.get(dependency.task_type, None)
            main_dependencies.append(database_id)

        task_instance = lookup_task if isinstance(lookup_task, Task) else Task[lookup_task.__name__]
        if not task_instance.should_run():
            return
        database_id = self.tasks_database_ids.get(lookup_task.task_type, None)
        if database_id:
            return
        self.tasks_database_ids[lookup_task.task_type] = randint(1, 1000)


class Task(ABC):
    task_type: str
    dependencies: list | None = None
    _database_id: str = ""
    _instances = {}

    def __new__(cls):
        instance = super().__new__(cls)
        cls._instances[cls.__name__] = instance
        return instance
    
    @classmethod
    def __class_getitem__(cls, class_name):
        return cls._instances[class_name]

    @abstractmethod
    def should_run(self) -> bool:
        ...

    @property
    def database_id(self):
        return self._database_id

    @database_id.setter
    def database_id(self, id: str):
        self._database_id = id

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
    all_tasks = [A(), B(), C(), D()]

    try:
        for i, task in enumerate(all_tasks):
            c.recursive_dependencies(task)
    except Exception as e:
        print("ERRRRRO", str(e))
        pass

    print(c.tasks_database_ids)
