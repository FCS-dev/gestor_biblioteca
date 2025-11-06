import os
import utils
import modelo


def main():
    """
    Funcion main() del gestor de biblioteca.
    """
    libros = utils.cargar_libros()
    while True:
        # Obtener cantidad de libros no disponibles (estado=False)
        cnt_prestados = sum([1 for libro in libros if not libro.estado])
        os.system("cls" if os.name == "nt" else "clear")
        variable = utils.mostrar_menu()
        match variable:
            case "1":  # Mostrar Libros
                modelo.mostrar_libros(libros, "t")
            case "2":  # Agregar nuevos Libros
                modelo.agregar_libro(libros)
            case "3":  # Prestar Libros
                if cnt_prestados < len(libros):
                    modelo.prestar_libro(libros)
                else:
                    print("\nNo hay libros disponibles para prestar")
            case "4":  # Devolver Libros
                if cnt_prestados > 0:
                    modelo.devolver_libro(libros)
                else:
                    print("\nNo hay libros pendientes para devolver")
            case "5":  # Buscar libros por autor
                # TODO
                modelo.buscar_libro_autor(libros)
            case "6":  # Guardar la lista en JSON y salir del app
                utils.guardar_info_json(libros)
                break
            case _:
                print("\nOpción no válida")
        input("\nPulse Intro para continuar")


if __name__ == "__main__":
    main()
