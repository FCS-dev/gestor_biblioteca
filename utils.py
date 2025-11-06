from pathlib import Path
import json


def mostrar_menu():
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
    from modelo import Libro

    DATA_PATH = Path(__file__).parent / "libros.json"
    libros_def = []
    if DATA_PATH.exists():
        try:
            with DATA_PATH.open("r", encoding="utf-8") as f:
                libros_def = json.load(f)
        except json.JSONDecodeError:
            print("ERROR: El archivo JSON está dañado o vacío.")
            return libros_def
        except Exception as e:
            print("ERROR inesperado:", type(e).__name__, e)
            return libros_def
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
    return libros_def
