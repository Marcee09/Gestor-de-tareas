import json
from tarea import Tarea

class GestorTareas:
    def __init__(self, archivo="tareas.json"):
        self.archivo = archivo
        self.tareas = self.cargar()

    def guardar(self):
        with open(self.archivo, "w") as f:
            json.dump([t.__dict__ for t in self.tareas], f, indent=2)

    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                return [Tarea(**t) for t in data]
        except FileNotFoundError:
            return []
    
    def agregar(self, titulo, descripcion):
        id = len(self.tareas) + 1
        tarea = Tarea(id, titulo, descripcion)
        self.tareas.append(tarea)
        self.guardar()

    def listar(self):
        for t in self.tareas:
            print(t)

    def marcar_hecha(self, id):
        for t in self.tareas:
            if t.id == id:
                t.hecha = True
        self.guardar()

    def eliminar(self, id):
        self.tareas = [t for t in self.tareas if t.id != id]
        self.guardar()
    