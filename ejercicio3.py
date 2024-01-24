v1=""
v2=""
v3=""
while v1==v2 or v1==v3 or v3==v2:
    v1=int(input("Hola, ingrese 3 voltajes distintos\n\tIngrese voltaje 1: "))
    v2=int(input(f"\tIngrese voltaje 2: "))
    v3=int(input(f"\tIngrese voltaje 3: "))
aver=(v1+v2+v3)/3
if aver<115:
    print(f"<VOLTAJE CORRECTO={aver}>")
elif aver>115 and aver<220:
    print(f"<ALTO VOLTAJE={aver}>")
else:
    print(f"<PELIGRO={aver}>")