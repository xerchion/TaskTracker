import json
import os


class File:
    def __init__(self, name) -> None:
        self.name = name

    def exists(self):
        return os.path.exists(self.name)

    def create(self, data):
        # crea un fichero en la carpeta acutal, con el nombre indicado.
        with open(self.name, "w") as file:
            # Añadir la nueva tarea a la lista de tareas
            json.dump(data, file, indent=4)

    def delete(self):
        if os.path.exists(self.name):
            os.remove(self.name)
        else:
            print(f"El archivo {self.name} no existe.")
            return False

    def save_data(self, data):
        # crea un fichero en la carpeta acutal, con el nombre indicado.
        with open(self.name, "w") as file:
            # Añadir la nueva tarea a la lista de tareas
            json.dump(data, file, indent=4)

    def extract_data(self):
        # extrae los datos del archivo json
        # el joson es una lista de diccionarios
        with open(self.name) as file:
            data = json.load(file)
        return data
