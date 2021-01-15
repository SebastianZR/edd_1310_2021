class Stack :
    def __init__ (self):
        self.__data = list ()

    def is_empty(self):
        return len(self.__data)==0

    def lenght (self):
        return len (self.__data)

    def pop (self):
        if self.is_empty ():
            print ("Pila vacia")
        else:
            return self.__data.pop()

    def push (self, value):
        self.__data.append (value)

    def peek (self):
        return self.__data[len(self.__data) -1]

    def to_string (self):
        for item in self.__data[::-1] :
            print (f"  |  {item}  |  ")
            print ("  -------  ")


def suma_lista_rec(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista.pop() + suma_lista_rec(lista)

def regresivo (num):
    if num >= 0 :
        print (num)
        regresivo(num-1)
    else:
        return None

def delate (pila,media):
    agregamos = pila.pop()

    if pila.lenght() != media :
        delate(pila,media)
    else:
        pila.pop()

    pila.push(agregamos)




def main3():

    pq = Stack()
    pq.push(1)
    pq.push(2)
    pq.push(3)
    pq.push(4)

    mitad = ( pq.lenght() / 2 )


    if (mitad % 2) != 0:
        mitad = int(mitad)

    delate(pq,mitad)
    pq.to_string()


def main1():
    datos = [4,2,3,5] # 14
    resultado = suma_lista_rec(datos)
    print(resultado)

def main2():
    regresivo(int(input("Ingresa un numero : ")))

#main1()
#main2()
main3()
