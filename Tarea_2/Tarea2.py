arch = open('Datos.txt', 'r')
linea1= arch.readline().lstrip().split(',')
arch.close()
for j in range (len (linea1)):
    linea1[j]=int(linea1[j].strip())
print (linea1)

def sumalista(listaNumeros):
   if len(listaNumeros) == 1:
        return listaNumeros[0]
   else:
        return listaNumeros[0] + sumalista(listaNumeros[1:])


