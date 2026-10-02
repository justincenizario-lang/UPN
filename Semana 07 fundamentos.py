
def censurar_resena(resena, prohibidas):
    """Reemplaza cada palabra prohibida por asteriscos de igual longitud.
    Python no tiene parámetros 'out': se devuelve una tupla (texto, censuras)."""
    censuras = 0

    for palabra in prohibidas:
        if not palabra.strip():
            continue

        # lower() + in para ignorar mayúsculas/minúsculas
        while palabra.lower() in resena.lower():
            pos = resena.lower().index(palabra.lower())
            # len() equivale a Length en C#
            resena = resena[:pos] + "*" * len(palabra) + resena[pos + len(palabra):]
            censuras += 1

    return resena, censuras


def main():
    prohibidas = ["estafa", "basura", "idiota", "horrible"]

    resena = input("Ingrese la reseña: ")
    resultado, total = censurar_resena(resena, prohibidas)

    print("\nReseña moderada:", resultado)
    print("Número de censuras aplicadas:", total)


if __name__ == "__main__":
    main()