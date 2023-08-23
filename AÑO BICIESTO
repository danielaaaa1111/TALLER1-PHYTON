# Pedir al usuario que ingrese el año
anno = int(input("Ingrese el año: "))

# Verificar si el año es bisiesto según las reglas del calendario gregoriano y juliano
es_bisiesto = False

# Verificar si el año cumple con las reglas del calendario juliano
if anno % 4 == 0:
    es_bisiesto = True

# Verificar si el año cumple con las reglas del calendario gregoriano
if anno % 100 == 0:
    if anno % 400 == 0:
        es_bisiesto = True
    else:
        es_bisiesto = False

# Mostrar el resultado
if es_bisiesto:
    print(f"{anno} es bisiesto")
else:
    print(f"{anno} no es bisiesto")
