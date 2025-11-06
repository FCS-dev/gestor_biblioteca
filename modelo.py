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
    mostrar_libros(libros, "p")
    str_id = input("\nId del libro que desea devolver: ").strip()
    try:
        id = int(str_id) - 1
    except ValueError:
        print("\nEl id indicado no es número")
        return
    id = int(str_id) - 1
    if 0 <= id < len(libros):
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
