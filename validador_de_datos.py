def validar_rut():
    rut = input("Ingrese su RUT sin puntos ni guion: ").strip()

    if rut.isdigit() and 8 <= len(rut) <= 9:
        return True
    else:
        print("RUT inválido.")
        return False


def validar_edad():
    edad = int(input("Ingrese su edad: "))

    if 18 <= edad <= 120:
        return True
    else:
        print("Edad inválida o menor de edad.")
        return False


def sistema():
    print("\n=== SISTEMA DE REGISTRO ===")

    rut_ok = validar_rut()
    edad_ok = validar_edad()

    if rut_ok and edad_ok:
        print("\n Validación correcta. Acceso permitido.")
    else:
        print("\n No cumple los requisitos.")


sistema()