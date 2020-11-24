class NodoDoble :
    def __init__ (self,value,siguiente=None,anterior=None):
        self.data = value
        self.next = siguiente
        self.prev = anterior

class DobleLinkedList :
    def __init__ (self):
        self.__head = NodoDoble(None)
        self.__tail = NodoDoble(None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0

    def is_empy (self):
        return self.__head.data == None

    def append (self,value):#Agrega un nodo al final entrando por head
        nuevo = NodoDoble (value)
        if self.is_empy() == True :
            self.__head = nuevo
            self.__tail = nuevo
        else :
            curr_node = self.__head
            while curr_node.next != None :
                curr_node = curr_node.next
            self.__tail= nuevo
            self.__tail.prev = curr_node
            curr_node.next = self .__tail

    def transversal (self):
        curr_node = self.__head
        while curr_node != None:
            print (f"{curr_node.data}-------->", end = " ")
            curr_node= curr_node.next
        print (" ")

    def reverse_transversal(self):
         curr_node = self.__tail
         while curr_node != None:
            print(f"{curr_node.data}-------->", end=" ")
            curr_node = curr_node.prev
         print(" ")

    def find_from_head (self,value):
        curr_node = self.__head
        posicion = 0
        while curr_node.data != value and curr_node.next != None :
            curr_node = curr_node.next
            posicion = posicion +1
        if curr_node.data == value:
            print ("DATO ENCONTRADO")
            print (f"En la posicion {posicion}")
        else:
            print ("Dato no encontrado")

    def find_from_tail (self,value):
        curr_node = self.__tail
        posicion = 0
        while curr_node.data != value and curr_node.prev != None :
            curr_node = curr_node.prev
            posicion = posicion + 1
        if curr_node.data == value:
            print ("DATO ENCONTRADO")
            print (f"En la posicion {posicion}")
        else:
            print ("Dato no encontrado")

    def remove_from_head(self, value):
        curr_node = self.__head

        if self.__head.data == value:
            self.__head = self.__head.siguiente
            self.__head.next = None
        else:

            while curr_node.data != value and curr_node.next != None:
                curr_node = curr_node.next
            if curr_node.data == value:
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev
            else:
                print ("Dato no encontrado")

    def remove_from_tail(self, value):
        curr_node = self.__tail
        if self.__tail.data == value :
            self.tail = self.__tail.prev
            self.__tail.next = None
        else :
            while curr_node.data != value and curr_node.prev != None :
                curr_node = curr_node.prev
            if curr_node.data == value :
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev
            else :
                print ("Dato no encontrado")
