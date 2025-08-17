class Tarea:
    def __init__(self, id, titulo, descripcion, hecha=False):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.hecha = hecha

    def __repr__(self):
        estado = "✅" if self.hecha else "❌"
        return f"[{estado}] {self.id} - {self.titulo}: {self.descripcion}"