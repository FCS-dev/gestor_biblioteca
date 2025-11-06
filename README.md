# Proyecto Gestión de Biblioteca con control de versiones

**Curso:**      Algorismica i programació amb Python
**Trabajo:**    PAC-1. Projecte Gestió de Biblioteca amb control de versions
**Profesor:**   Manel Plaza
**Autores:**    Javier Lorca
                Franco Calderón Sánchez
**Lugar:**      CIFO La Violeta, Barcelona
**Fecha:**      06 Noviembre del 2025

---

## Distribución del trabajo comprendido

**Class Libro** - Franco
**R/W "catalogo.json"** - Franco
**menu.py** - Javier
**agregar_libro()** - Franco
**prestar_libro()** - Javier
**devolver_libro()** - Franco
**buscar_libro_autor()** - Javier
**mostrar_libros()** - Franco / Javier
**(elaboración) README.md** - Franco / Javier

---

## Uso de la IA

### Motor usado: *www.chatgpt.com*

### Pregunta a chatgpt por un error al momento de grabar un archivo .JSON

- Al probar la funcionalidad de grabar el archivo **"catalogo.json"**, destinado a almacenar la lista de libros con sus respectivos **estados** (disponible o prestado), se presentó un error que motivó la consulta a la IA de **ChatGPT**.
La respuesta fue clara y precisa: los archivos **JSON** que se utilizan para persistencia deben contener **listas de diccionarios**, no listas de clases (como se manejaba originalmente en el aplicativo).
En consecuencia, se implementó una rutina que convierte previamente la lista de objetos de la clase **"Libro"** en una lista de diccionarios con los mismos atributos (las *keys* que definen la estructura de los diccionarios).
Este mismo procedimiento se aplica de forma inversa al leer un archivo **.json** existente: la lista de diccionarios se transforma nuevamente en una lista de objetos de la clase **"Libro"**.

**Prompt** (aproximado):
"Python. Error al escribir archivo JSON. El mensaje de error: "TypeError: Object of type Libro is not JSON serializable".
Código:
```python
def guardar_info_json(libros):
    try:
        with DATA_PATH.open("w", encoding="utf-8") as f:
            json.dump(libros, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("ERROR inesperado:", type(e).__name__, e)
```
 Analiza el codigo y el error, y dime que puede estar pasando"

**Respuesta** (Extracto):
"El error ocurre porque los objetos de una clase no pueden serializarse directamente a JSON.
La solución es convertir cada objeto Libro en un diccionario antes de guardarlo (obj.__dict__ o un método to_dict()), y al leer el archivo JSON, reconstruir la lista de objetos creando nuevas instancias de Libro a partir de esos diccionarios."

**Solución final**
- Con ese conocimiento, el código se complementó y las funciones implicadas quedaron así:
```python
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
```

---

## 📚 Módulos de Python usados

- Módulo **Path** de la libreria **pathlib**: Para definir la ruta donde se ubica el archivo catalogo.json
- Módulo **json**: Para operaciones (lectura y escritura) de archivos **.JSON**
- Módulo **os**: Para, con las funciones del S.O., poder limpiar la pantalla del terminal (**'cls'** o **'clear'**)

---
