from colas import Queue
from colas import BoundedPriorityQueue

q1 = Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
print(q1.to_string())

print ("Prueba 2 Queue")
c1 = {"id" : 1 ,"nombre":"Mario" , "balance":20.5}
c2 = {"id" : 2 ,"nombre":"Diana" , "balance":3456.5}
c3 = {"id" : 3 ,"nombre":"Bartolo" , "balance":100000000.0}

atencion = Queue ()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)

print (atencion.to_string())
siguiente = atencion.dequeue()
print (f"Bienvenido senor : {siguiente['nombre']}, en que podemos servirle el dia de hoy ")

print ("\n---------------------------------------------------------------------")
print("Pruebas de las colas con prioridad acotada")

maestres = {"prioridad":4 , "descripcion":"Maestre" , "personas":["Juan P", "Diego H"]}
ninos = {"prioridad":2 , "descripcion":"Niños" , "personas":["Santi H", "Angel H"]}
mecanicos = {"prioridad":4 , "descripcion":"Mecanicos" , "personas":["Diana T", "Maria Z"]}
mujeres = {"prioridad": 3, "descripcion":"Mujeres", "Personas":["Jennifer Z", "Rosario R"]}
terceraEdad = {"prioridad":2,"descripcion":"TerceraEdad","personas":["Natividad H","Alberto D"]}
ninas = {"prioridad": 1 , "descripcion": "Niñas" , "personas": ["Sofia M" , "Jeylin P"]}
hombres = {"prioridad": 3, "descripcion":"Hombres", "Personas":["Sebastian Z", "Gael H"]}
vigia = {"prioridad": 4, "descripcion":"Vigia", "Personas":["Enrique S","Ricardo N"]}
capitan = {"prioridad": 5, "descripcion":"Capitan", "Personas":["Andrea G"]}
timonel = {"prioridad": 4, "descripcion":"Timonel", "Personas":["Alitzel R", "Mario D"]}

cpa = BoundedPriorityQueue( 7 )

cpa.enqueue(maestres['prioridad'] , maestres)
cpa.enqueue(ninos['prioridad'] , ninos)
cpa.enqueue(mecanicos['prioridad'] , mecanicos)
cpa.enqueue(mujeres['prioridad'], mujeres)
cpa.enqueue(terceraEdad['prioridad'], terceraEdad)
cpa.enqueue(ninas['prioridad'],ninas)
cpa.enqueue(hombres['prioridad'],hombres)
cpa.enqueue(vigia['prioridad'],vigia)
cpa.enqueue(capitan['prioridad'],capitan)
cpa.enqueue(timonel['prioridad'],timonel)

cpa.to_string()

print(f"El barco esta vacio ? : {cpa.is_empty()}")

while cpa.is_empty()==False:
    cpa.dequeue()
else:
    print(f"Barco vacio")
    
print(f"El barco esta vacio ? : {cpa.is_empty()}")
