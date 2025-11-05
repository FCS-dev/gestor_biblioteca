import os
import utils
import modelo
# ToDo Readme


def main():
    # ToDo cargar_libros                                            # Franco
    libros = utils.cargar_libros()

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        # ToDo Menu
        variable = utils.mostrar_menu()  # Javier [✅]
        match variable:
            case "1":
                modelo.mostrar_libros(libros)  # Franco
            case "2":
                # TODO Agregar libros en modelo una funcion
                modelo.agregar_libro(libros)
            case "3":  # Javier
                # TODO Prestar
                modelo.prestar_libro(libros)
            case "4":  # Franco
                # TODO
                modelo.devolver_libro(libros)
            case "5":  # Javier
                # TODO
                modelo.buscar_libro_autor(libros)
            case "6":  # Franco
                # TODO Agregar libros
                modelo.guardar_info_json(libros)
                break
            case _:  # Javier
                print("\nOpcion no válida")
        input("\nPulse Intro para continuar")


if __name__ == "__main__":
    main()
