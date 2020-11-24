from arrays import Array

archivo = open("junio.dat","r")
empleado = archivo.readlines()
empleado = [e.replace('','').strip().split(',') for e in empleado]
lista = len(empleado)
empleados = Array(lista)

for x in range(1, lista):
    empleados.set_item(empleado[x], x)

print("Sueldos")
for x in range(1, lista):
    extra = float(276.5)
    hora_extra = float(empleados.get_item(x)[4])
    año_ingreso = float(empleados.get_item(x)[6])
    sueldo = float(empleados.get_item(x)[5])
    sueldo_extra = sueldo + (hora_extra * extra)
    sueldo_prestacion = (2020 - año_ingreso) * 0.03
    sueldo_total = float((sueldo*sueldo_prestacion)+sueldo_extra)
    print(f" N. empleado:{empleado[x][0]} Nombre:{empleado[x][1]} {empleado[x][2]} {empleado[x][3]} sueldo total de ${sueldo_total}")

print("\nEMPLEADOS CON MENOR ANTIGUEDAD")
for x in range(1, lista):
    if int(empleados.get_item(x)[6]) == 2020:
        print(f" N. empleado:{empleado[x][0]} Nombre: {empleado[x][1]} {empleado[x][2]} {empleado[x][3]}, Año de ingreso:{empleado[x][6]}")

print("\nEMPLEADOS CON MAYOR ANTIGUEDAD")
for x in range(1, lista):
    if int(empleados.get_item(x)[6]) == 2016:
        print(f" N. empleado:{empleado[x][0]} Nombre: {empleado[x][1]} {empleado[x][2]} {empleado[x][3]}, Año de ingreso:{empleado[x][6]}")


   

    

