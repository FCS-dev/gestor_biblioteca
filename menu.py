import os
import utils
import modelo


def main():
    libros = utils.cargar_libros()
    while True:
        cnt_prestados = sum([1 for libro in libros if not libro.estado])
        os.system("cls" if os.name == "nt" else "clear")
        variable = utils.mostrar_menu()
        match variable:
            case "1":
                modelo.mostrar_libros(libros, "t")
            case "2":
                modelo.agregar_libro(libros)
            case "3":  # Javier
                # TODO Prestar
                if cnt_prestados < len(libros):
                    modelo.prestar_libro(libros)
                else:
                    print("\nNo hay libros disponibles para prestar")
            case "4":
                if cnt_prestados > 0:
                    modelo.devolver_libro(libros)
                else:
                    print("\nNo hay libros pendientes para devolver")
            case "5":  # Javier
                # TODO
                modelo.buscar_libro_autor(libros)
            case "6":
                utils.guardar_info_json(libros)
                break
            case _:
                print("\nOpción no válida")
        input("\nPulse Intro para continuar")


if __name__ == "__main__":
    main()
