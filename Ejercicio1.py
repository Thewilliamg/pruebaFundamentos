v1=int(input("Ingrese voltaje 1: "))
v2=int(input("Ingrese voltaje 2: "))
v3=int(input("Ingrese voltaje 3: "))
v4=int(input("Ingrese voltaje 4: "))
v5=int(input("Ingrese voltaje 5: "))
promedio=(v1+v2+v3+v4+v5)/5
if promedio>220:
    print(f"<ALTO VOLTAJE={promedio}>")
else:
    print(f"<VOLTAJE CORRECTO={promedio}>")
