l=int(input("Hola, ingrese el tamaño del lado del triangulo equilatero: "))
base=l
altura=(l**2-(base/2)**2)**0.5
area=base*altura/2
if area>1000:
    print(f"<DATOS NO VÁLIDOS={area}")


