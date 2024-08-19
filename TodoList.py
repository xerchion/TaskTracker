import time
from typing import List

from constants import INC, LAST, USER_MSG
from Task import Task


class TodoList:
    def __init__(self, data) -> None:
        self.tasks: List[Task] = []
        self.to_tasks(data)

    def get_new_id(self) -> int:
        # return:  A new id for the task
        if len(self.tasks) == 0:
            new_id = 1
        else:
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
        task = self.get_task_by_id(id)
        index = self.get_index(task)
        self.tasks[index].set_description(new_text)
        self.tasks[index].set_updated_at(time.time())

    def delete_task(self, id: int):
        # Returns false if the task does not exist.
        # ! quitar este for y cambiar por buscar....
        for task in self.tasks:
            if task.get_id() == id:
                index = self.tasks.index(task)
                del self.tasks[index]
                return True
        return False

    def mark_task(self, id, option):
        # Changes status´s task
        task = self.get_task_by_id(id)
        index = self.get_index(task)
        self.tasks[index].set_status(option)
        self.tasks[index].set_updated_at(time.time())

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

    def prepare_view(self, data):
        # Muestra la lista de tareas que recibe por parametro
        # Puede obtener una sola tarea o una lista de ellas
        result = "\n\n" + "-" * 100
        result = result + "\n" + USER_MSG["HEADER_LIST"] + "\n"
        result = result + "-" * 100 + "\n"
        if type(data) is Task:
            result = result + data.to_string()
        else:
            for task in data:
                result = result + "\n" + task.to_string()
        result = result + "\n" + "_" * 100 + "\n"
        return result

    def size(self):
        return len(self.tasks)

    def task_exists(self, text):
        for task in self.tasks:
            if task.get_description() == text:
                return task
        return False

    def get_task_by_description(self, task_name: str):
        return next(
            (task for task in self.tasks if task.get_description() == task_name), None
        )

    def get_task_by_id(self, id: int):
        # Return task with this id, else None
        for task in self.tasks:
            if task.get_id() == id:
                return task
        return None

    def get_index(self, task: Task) -> int:
        return self.tasks.index(task)

    def get_tasks(self):
        return self.tasks
