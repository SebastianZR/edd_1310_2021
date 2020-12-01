class Nodo :
    def __init__ (self , value, siguiente=None):
        self.data = value
        self.siguiente = siguiente
class CircularList :
    def __init__ (self):
        self.__ref = None
        self.__size = 0

    def is_empty (self):
        return self.__ref == None

    def insert (self,value):

        if self.is_empty():
            nuevo = Nodo(value, None)
            nuevo.siguiente = nuevo
            self.__ref = nuevo
            self.__size += 1
        elif self.search(value) == False:
            if value < self.__ref.siguiente.data:
                self.__ref.siguiente = Nodo(value, self.__ref.siguiente)
                self.__size += 1
            elif value > self.__ref.data:
                self.__ref.siguiente = Nodo(value, self.__ref.siguiente)
                self.__ref = self.__ref.siguiente
                self.__size += 1
            else:
                curr_node = self.__ref
                while value > curr_node.siguiente.data:
                    curr_node = curr_node.siguiente
                curr_node.siguiente = Nodo(value, curr_node.siguiente)
                self.__size += 1
        else:
            print("El dato ya esta en la lista")

    def search (self, value):
        busca = False
        if self.is_empty():
            print ("Lista Vacia")
        else :
            curr_node = self.__ref.siguiente
            while curr_node.data != value and curr_node.data != self.__ref.data:
                curr_node = curr_node.siguiente
            if curr_node.data ==  value:
                busca = True
            else :
                busca = False

            return busca

    def transversal( self ):
        curr_node = self.__ref.siguiente
        while curr_node.data != self.__ref.data:
            print(f"{curr_node.data}--->", end="")
            curr_node = curr_node.siguiente
        print(f"{self.__ref.data}--->")

    def remove(self, value):
        if self.search(value) == True :
            anterior = self.__ref
            curr_node = self.__ref.siguiente
            while curr_node.data != value :
                anterior = curr_node
                curr_node = curr_node.siguiente
            anterior.siguiente = curr_node.siguiente
            self.__size -= 1
            if value == self.__ref.data:
                self.__ref = anterior
                self.__size -= 1
        else:
            print (" El valor no esta en la lista ")



    def size (self):
        return "Tamanio de lista : ", self.__size
