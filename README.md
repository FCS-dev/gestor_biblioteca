# Projecte Gestió de Biblioteca amb control de versions

**Curso:** Algorismica i programació amb Python
**Trabajo:** PAC-1. Projecte Gestió de Biblioteca amb control de versions
**Profesor:** Manel Plaza
**Autor:**  Javier Lorca
            Franco Calderón Sánchez
**Lugar:** CIFO La Violeta, Barcelona
**Fecha:** 06 Noviembre del 2025

---
## Distribución del trabajo:

**Class Libro()** - Franco
Lectura/Escritura "catalogo.json" - Franco
menu.py - Javier
agregar_libro - Franco
prestar_libro - Javier
devolver_libro - Franco
buscar_libro_autor - Javier
mostrar_libros - Franco / Javier
elaboración README.md - Franco / Javier
---

## Uso de la IA

### Consulta sobre funcionalidades de tratamiento de archivos .CSV

- Desconocía una forma óptima de escribir un archivo .CSV en disco a partir de una lista (**List**) de diccionarios (**{}**) de **Python**; adecuando una estructura con data de prueba y buscando la manera mas simple de subir la info al archivo gestionado, encontré dos sentencias que se adecuaron muy bien a lo que estaba buscando.

**Prompt** (aproximado):
"Python. Formas de crear un archivo .CSV, cargando una lista de diccionarios para persistencia."

**Respuesta** (Extracto de lo aprovechado):
"Forma recomendada (y alineada (hasta la fecha) con el curso):

```python
import csv
# Lista de diccionarios (cada dict es una fila)
productos = [
    {"id": 1, "nombre": "Mouse", "precio": 25.5, "cantidad": 10},
    {"id": 2, "nombre": "Teclado", "precio": 45.0, "cantidad": 5},
    {"id": 3, "nombre": "Monitor", "precio": 200.0, "cantidad": 2},
]

# Nombre del archivo
NOMBRE_ARCHIVO = "productos.csv"

# Obtener los nombres de las columnas (claves del primer diccionario)
campos = ["id","nombre","precio","cantidad"]

# Escribir el archivo
with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()         # Escribe los encabezados
    writer.writerows(productos)  # Escribe todas las filas

print("✅ Archivo CSV creado correctamente.")
```

Otra forma -> Usando pandas (más potente, pero requiere instalación)....- Descartado por el momento-
"

---

## 📈 Aplicación

- Con la estructura definida por defecto, decidí incluir la función:

```python
csv.DictWriter(f, fieldnames=columnas)
```

para definir el nombre de las columnas que debería llevar el .CSV. Y luego incluir las sentencias:

```python
writer.writeheader()
writer.writerows(productos)
```

Para hacer una escritura en bloque de la info que requería el funcionamiento de la app cuando el se dé el caso que no haya un un archivo .CSV en el directorio previo al inicio de la app.

## 📚 Referencias

- www.chatgpt.com

---
