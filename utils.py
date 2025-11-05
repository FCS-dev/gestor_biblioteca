
def mostrar_menu():
    print('''
          \n
------ GESTOR DE BIBLIOTECA -----
              MENU
|===============================|
|    1. Mostrar Libros          |
|    2. Agregar Libro           |
|    3. Prestar Libro           |
|    4. Devolver Libro          |
|    5. Buscar Libro por Autor  |
|    6. Salir y guardar en JSON |
|===============================| 
          ''')
    
    opcion = input("Ingrese su opcion -> ").strip()
    
    return opcion
    
def cargar_libros():
    pass 
    # Verificamos si existe un archivo JSON si existe coger los datos del archivo como iniciales
    # ELSE: generar un archivo con un lista predeterminada
    # RETURN "una lista de libros"
    return []