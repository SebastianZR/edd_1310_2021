from colas import Queue

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


print("Pruebas de las colas con prioridad acotada")

maestres = {"prioridad":4 , "descripcion":"Maestre" , "personas":["Juan P", "Diego H"]}
niños = {"prioridad":2 , "descripcion":"Niños" , "personas":["Santi H", "Angel H"]}
mecanicos = {"prioridad":4 , "descripcion":"Mecanicos" , "personas":["Diana T", "Maria Z"]}

cpa = BoundedPriorityQueue( 7 )
cpa.enqueue(maestres['prioridad'] , maestres)
cpa.enqueue(niños['prioridad'] , niños)
cpa.enqueue(mecanicos['prioridad'] , mecanicos)
cpa.to_string()
