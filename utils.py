
def mostrar_menu():
    print('''
          \n --- GESTOR DE VIAJES ---
          1. Agretar libro
          2. Buscar Libro por Autor
          3. Guardar Informacion
          ''')
    opc=input("INgrese su opcion -> ")
    return opc

def cargar_libros():
    pass 
    # Verificamos si existe un archivo JSON si existe coger los datos del archivo como iniciales
    # ELSE: generar un archivo con un lista predeterminada
    # RETURN "una lista de libros"
    return []