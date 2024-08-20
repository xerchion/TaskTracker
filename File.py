import json
import os


class File:
    def __init__(self, name) -> None:
        self.name = name

    def exists(self):
        return os.path.exists(self.name)

    def delete(self):
        if os.path.exists(self.name):
            os.remove(self.name)
        else:
            print(f"El archivo {self.name} no existe.")
            return False

    def save_data(self, data):
        with open(self.name, "w") as file:
            json.dump(data, file, indent=4)

    def extract_data(self):
        with open(self.name) as file:
            data = json.load(file)
        return data
