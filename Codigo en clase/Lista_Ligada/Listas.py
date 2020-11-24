class Nodo :
    def __init__ (self , value , siguiente=None ):
        self.data = value
        self.siguiente = siguiente
class LinkedList :
    def __init__ (self):
        self.__head = None
    def is_empy (self):
        return self.__head == None

    def append (self,value):
        nuevo = Nodo (value)
        if self.__head == None:
            self.__head = nuevo
        else :
            curr_node = self.__head
            while curr_node.siguiente != None:
                curr_node = curr_node.siguiente
            curr_node.siguiente = nuevo

    def transversal (self):
        curr_node = self.__head
        while curr_node != None:
            print (f"{curr_node.data}----> ", end="" )
            curr_node = curr_node.siguiente

    def remove (self, value):
        curr_node = self.__head
        anterior = None
        if self.__head.data == value :
            self.__head = self.__head.siguiente
        else:
            while curr_node.data != value and curr_node.siguiente != None:
                anterior = curr_node
                curr_node = curr_node.siguiente
            if curr_node.data == value:
                anterior.siguiente = curr_node.siguiente
            else :
                 print (" El dato no existe en la lista")

    def prepend (self,value):
        nuevo = Nodo (value, self.__head)
        self.__head = nuevo

    def tail (self):
        curr_node = self.__head
        while curr_node.siguiente != None:
            curr_node = curr_node.siguiente
        return curr_node

    def get (self , posicion=None):
        contador = 0
        dato = None

        if posicion == None :
            dato  = self.tail().data
        else :
            curr_node = self.__head
            while contador != posicion:
                contador = contador + 1
                curr_node = curr_node.siguiente
            if contador == posicion:
                dato = curr_node.data
            else :
                print (" No existe esa posicion en la lista ")
        return dato
