def main():
    try:
        # Solicitar dos números enteros al usuario
        dividendo = int(input("Ingrese el dividendo (número a dividir): "))
        divisor = int(input("Ingrese el divisor (número por el cual dividir): "))

        igual = dividendo / divisor

        if dividendo % divisor == 0:
            exacta_division = True
        else:
            exacta_division = False

        print(f"Resultado de la división: {igual}")

        if exacta_division:
            print("La división es exacta.")
        else:
            print("La división no es exacta.")


