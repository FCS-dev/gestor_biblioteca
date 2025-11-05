class Libro:
    def __init__(self, titulo, autor, anio, estado):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.estado= estado
    
    def __repr__(self):
        return f'Libro("{self.titulo}", "{self.autor}", {self.anio}, "{self.estado}")'
    
    def cambiar_estado(self):
        self.estado = not self.estado
        
    # ToDo crear una clase con la cual crear clase
    
def agregar_libro(libros):
    pass

def prestar_libro(libros):
    pass                

def devolver_libro(libros):
    pass

def buscar_libro_autor(libros):
    pass

def guardar_info_json(libros):
    pass

def mostrar_libros():
    pass