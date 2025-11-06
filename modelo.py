class Libro:
    def __init__(self, titulo, autor, anio, estado=True):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__estado = estado

    def __repr__(self):
        return f'Libro("{self.__titulo}", "{self.__autor}", {self.__anio}, "{self.__estado}")'

    def cambiar_estado(self):
        self.__estado = not self.__estado

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        if titulo:
            self.__titulo = titulo
        else:
            print("Titulo no puede ser vacio")

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        if autor:
            self.__autor = autor
        else:
            print("Autor no puede ser vacio")

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, anio):
        if anio > 1500:
            self.__anio = anio
        else:
            print("El año debe ser mayor a 1500")

    @property
    def estado(self):
        return self.__estado


def agregar_libro(libros):
    pass


def prestar_libro(libros):
    try:
        seleccion = int(
            input("seleccione el numero de libro que quere tomar prestado: ")
        )
        seleccion -= 1
        libros[seleccion].cambiar_estado()
    except ValueError:
        print("seleccion no válida")

    return seleccion


def devolver_libro(libros):
    pass


def buscar_libro_autor(libros):
    try:
        seleccion = input("Ingrese el nombre del Autor: ").strip().lower()
        indices_encontrados = [ i for i, libro in enumerate(libros) if libro.autor.lower() == seleccion]  
        #CHATGPT tengo una lista con objetos y quiero buscar el indice del objeto segun un atributo del mismo python
        # https://gemini.google.com/share/c2e90d768fd3 link de acceso a CHAT GPT
        
        libros_autor = []  
             
        for indice in indices_encontrados:
            autor = libros[indice].titulo
            
            libros_autor.append(autor)

    except:
        print("Autor no encontrado")
        
    return libros_autor
        
def mostrar_lista(lista):
    if not lista:
        print('no hay libros para el autor buscado')
    else:
        print('\nListado de libros del autor buscado\n')
        for i, elemento in enumerate(lista):
            print(f'{i+1} - {elemento}') 
        


def guardar_info_json(libros):
    pass


def mostrar_libros(libros):
    if libros:
        print(
            "Autor                  Titulo                 Año    Estado"
            "\n-----------------------------------------------------------"
        )
        for l in libros:
            estado = "Disponible" if l.estado else "Prestado"
            print(f"{l.autor.ljust(20)} {l.titulo.ljust(20)} ({l.anio}) => {estado}")
    else:
        print("\nNo hay libros para mostrar")
