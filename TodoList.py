import time
from typing import List

from constants import INC, LAST
from Task import Task


class TodoList:
    def __init__(self, data) -> None:
        self.tasks: List[Task] = []
        self.to_tasks(data)

    def get_new_id(self) -> int:
        # return:  A new id for the task
        new_id = self.tasks[LAST].get_id() + INC
        while self.id_exists(new_id):
            new_id += INC
        return new_id

    def id_exists(self, id: int) -> bool:
        return any(task.get_id() == id for task in self.tasks)

    def add_task(self, text):
        id = self.get_new_id()
        now = time.time()
        new_task = Task(id, text, "todo", now, now)
        self.tasks.append(new_task)

    def update_task(self, id, new_text):
        self.tasks[id].set_description(new_text)
        self.tasks[id].set_updated_at(time.time())

    def delete_task(self, id):
        # Returns false if the task does not exist.
        for task in self.tasks:
            if task.get_id() == id:
                index = self.tasks.index(task)
                del self.tasks[index]
                return True
        return False

    def mark_task(self, id, option):
        # Changes status´s task
        self.tasks[id].set_status(option)
        self.tasks[id].set_updated_at(time.time())

    def filter_by(self, filter):
        filtered_tasks = []
        if filter == "all":
            filtered_tasks = self.tasks
        else:
            for task in self.tasks:
                if task.get_status() == filter:
                    filtered_tasks.append(task)
        return filtered_tasks

    def to_tasks(self, data):
        # parametros: data tipo diccionario
        # convierta el dato recibido a la clase Task
        #           y lo agrega a la lista de Tasks
        for task in data:
            self.tasks.append(
                Task(
                    int(task["id"]),
                    task["description"],
                    task["status"],
                    task["created_at"],
                    task["updated_at"],
                )
            )

    def to_dict(self):
        # convierta la lista de objetos Tasks en una lista de diccionarios
        # return: la lista de diccionarios
        list_dict_task = []
        for task in self.tasks:
            list_dict_task.append(task.to_dict())
        return list_dict_task

    def view(self, data):
        # Muestra la lista de tareas que recibe por parametro
        # Puede obtener una sola tarea o una lista de ellas
        print("\n\n" + "-" * 100)
        print(
            "Id            Decription                    Status             Created             Updated"
        )
        print("-" * 100 + "\n")
        if type(data) is Task:
            print(data.to_string())
        else:
            for task in data:
                print(task.to_string())
        print("_" * 100 + "\n")

    def size(self):
        return len(self.tasks)

    def task_exists(self, text):
        for task in self.tasks:
            if task.get_description() == text:
                return task
        return False

    def get_task(self, task_name: str):
        return next(
            (task for task in self.tasks if task.get_description() == task_name), None
        )
