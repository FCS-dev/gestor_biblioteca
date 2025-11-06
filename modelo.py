"""
Clase base "Libro()"
\nAtributos:
__titulo: Título del libro
__autor: Autor del libro
__anio: Año del libro
__estado: True si esta disponible (para prestar). False si NO estya disponible.
"""


class Libro:
    def __init__(self, titulo, autor, anio, estado=True):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__estado = estado  # True = Disponible / False = No disponible

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
    """
    Función. Pide información para registrar un libro nuevo, y lo agrega a la lista general.
    \nParámetros:
    'libros'. List. Lista de libros
    """
    print("\n--- Agregar Libro ---")
    titulo = input("\nTítulo     : ").strip()
    autor = input("Autor      : ").strip()
    str_anio = input("Año (+1500): ").strip()
    # Validación: str_anio debe ser un int
    try:
        anio = int(str_anio)
    except ValueError:
        print("El año indicado no es válido")
        return
    # Validación: titulo y autor deben tener contenido
    if titulo and autor:
        # Validación: anio debe ser +1500
        if anio < 1500:
            print("El año debe ser mayor a 1500")
            return
        libros.append(Libro(titulo, autor, anio))
        print(f"\nEl libro '{titulo}' ha sido agregado correctamente")
    else:
        print("\nDatos incompletos. Proceso cancelado.")
        return


def prestar_libro(libros):
    """
    Función. Registrar prestar un libro.
    Cambiar estado de un libro de disponible (True) a no disponible (False).
    \nParámetros:
    'libros'. List. Lista de libros
    """
    print("\n---Opcion 3 Prestar Libro---")
    mostrar_libros(libros, "d")  # Listar libros disponibles
    try:
        seleccion = int(
            input("seleccione el numero de libro que quere tomar prestado: ")
        )
        if (
            0 < seleccion <= len(libros)
        ):  # Valida seleccion este en el rango (indice) de libros
            if libros[
                seleccion - 1
            ].estado:  # Valida que el libro indicado este disponible para prestar
                libros[seleccion - 1].cambiar_estado()
            else:
                print("El libro no esta disponible")
        else:
            print("Seleccion fuera de rango")
    except ValueError:
        print("seleccion no válida")


def devolver_libro(libros):
    """
    Función. Registrar devolver un libro.
    Cambiar estado de un libro de no disponible (False) a disponible (True).
    \nParámetros:
    'libros'. List. Lista de libros
    """
    mostrar_libros(libros, "p")  # Listar libros disponibles
    str_id = input("\nId del libro que desea devolver: ").strip()
    try:
        id = int(str_id) - 1
    except ValueError:
        print("\nEl id indicado no es número")
        return
    id = int(str_id) - 1
    if 0 <= id < len(libros):  # Valida id este en el rango (indice) de libros
        esta_prestado = libros[id].estado
        if (
            not esta_prestado
        ):  # Para devolver el libro, debe estar prestado (estado=False)
            libros[id].cambiar_estado()
            print(f"\nEl libro: '{libros[id].titulo}', ha sido marcado como devuelto")
        else:
            print("\nEl libro indicado no esta pendiente de devolución")
    else:
        print("\nEl id indicado no es número válido")


def buscar_libro_autor(libros):
    """
    Función. Buscar libros disponibles por 'Autor'.
    Muestra listado con los resultados.
    \nParámetros:
    'libros'. List. Lista de libros
    """
    autor_buscar = input("Ingrese el nombre del Autor: ").strip().lower()
    if not autor_buscar:  # Valida se ingrese al menos 1 caracter
        print("Debe introducir un texto para buscar")
        return
    # Generamos una sub-lista con los libros que contienen el autor segun la búsqueda
    listado_resultado = [
        elemento for elemento in libros if autor_buscar in elemento.autor.lower()
    ]
    if not listado_resultado:
        print("Autor no encontrado")
    else:
        mostrar_libros(listado_resultado, "f")  # Mostramos lista resultado


def mostrar_libros(libros, alcance="t"):
    """
    Función. Imprime lista de libros según parámetros recibidos.
    \nParámetros:
    - 'libros'. List. Lista de libros a mostrar.
    - 'alcance'. Str. Para adecuar el título del listado según corresponda:
        - "t": Todos los libros
        - "p": libros prestados
        - "d": libros disponibles
        - "f": libros con filtro (Buscar)
    """
    if libros:
        match alcance:
            case "t":  # Todos los libros
                titulo = "\n--- Listado de libros ---"
            case "p":  # libros prestados
                titulo = "\n--- Libros prestados ---"
            case "d":  # libros disponibles
                titulo = "\n--- Libros disponibles ---"
            case "f":  # libros con filtro (Buscar)
                titulo = "\n--- Libros encontrados ---"
            case _:
                print("\n(ERROR: Alcance no válido!!!)")
                return
        print(titulo)
        print(
            "Id  Autor                          Titulo                           Año      Estado"
            "\n-----------------------------------------------------------------------------------"
        )
        for idx, li in enumerate(libros):
            if (
                alcance == "p" and li.estado
            ):  # se pide "Pendientes" pero estado es True => no listar (continue)
                continue
            if (
                alcance == "d" and not li.estado
            ):  # se pide "Disponibles" pero estado es False => no listar (continue)
                continue
            indice = str(idx + 1)
            autor = li.autor[:30]
            libro = li.titulo[:30]
            anho = li.anio
            estado = "Disponible" if li.estado else "Prestado"
            print(
                f"{indice.ljust(2)}  {autor.ljust(30)} {libro.ljust(30)}   {anho} => {estado}"
            )
    else:
        print("\nNo hay libros para mostrar")
