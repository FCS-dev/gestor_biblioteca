from pathlib import Path
import json
from modelo import Libro

# Ruta y nombre del archivo donde se persiste el json
DATA_PATH = Path(__file__).parent / "catalogo.json"


def mostrar_menu():
    """
    Método. Muestra el menú de opciones y devuelve la opción elegida.
    \nRetorno:
    - 'opcion'. Str. Opción elegida.
    """
    print("""
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
          """)
    opcion = input("Ingrese su opcion -> ").strip()
    return opcion


def cargar_libros():
    """
    Método. Comprueba si existe el archivo "catalogo.json" en la ruta
    del aplicativo. Si existe, lee la info y retorna una lista.
    Si no existe, genera una lista (predeterminada).
    La lista contiene las instancias de la clase Libro().
    \nRetorno:
    - 'libros_def'. List. Lista de libros.
    """
    libros_def = []
    if DATA_PATH.exists():
        try:
            with DATA_PATH.open("r", encoding="utf-8") as f:
                libros_con_dict = json.load(f)
        except json.JSONDecodeError:
            print("ERROR: El archivo JSON está dañado o vacío.")
            return []
        except Exception as e:
            print("ERROR inesperado:", type(e).__name__, e)
            return []
    else:
        libros_def = [
            Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, True),
            Libro("Hamlet", "William Shakespeare", 1603, True),
            Libro("Orgullo y prejuicio", "Jane Austen", 1813, True),
            Libro("Crimen y castigo", "Fiódor Dostoyevski", 1866, True),
            Libro("Moby Dick", "Herman Melville", 1851, True),
            Libro("Cien años de soledad", "Gabriel García Márquez", 1967, True),
            Libro("1984", "George Orwell", 1949, True),
            Libro("En busca del tiempo perdido", "Marcel Proust", 1913, True),
            Libro("Ulises", "James Joyce", 1922, True),
            Libro("El señor de los anillos", "J. R. R. Tolkien", 1954, True),
            Libro("Otro libro de Jane Austen", "Jane Austen", 1813, True),
        ]
    for li in libros_con_dict:
        libros_def.append(Libro(li["titulo"], li["autor"], li["anio"], li["estado"]))
    return libros_def


def guardar_info_json(libros):
    """
    Función. Graba en el "catalogo.json" la lista de libros, con sus estados actualizados.
    Las lista en el app se guardan con clases Libro(), por lo que previamente se convierte
    a una lista de diccionarios ("libros_json")
    """
    # Convirtiendo cada class Libro() (los elementos de la lista "libros"),
    # en diccionarios, y agregarlos a una nueva lista libros_json
    libros_json = []
    for li in libros:
        libro_dict = {
            "titulo": li.titulo,
            "autor": li.autor,
            "anio": li.anio,
            "estado": li.estado,
        }
        libros_json.append(libro_dict)
    try:
        with DATA_PATH.open("w", encoding="utf-8") as f:
            json.dump(libros_json, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("ERROR inesperado:", type(e).__name__, e)
