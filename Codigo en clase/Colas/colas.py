class Queue :
    def __init__ (self):
        self.__data = list()

    def is_empty(self):
        return len(self.__data)==0

    def lenght (self):
        return len(self.__data)

    def enqueue(self,elem):
        self.__data.append(elem)

    def dequeue (self):
        if not self.is_empty():
            return self.__data.pop(0)
        else:
            return None

    def to_string (self):
        cadena = ""
        for elem in self.__data :
            cadena = cadena + " | "+ str(elem)
        cadena = cadena + " | "
        return cadena

#property Queue
class PriorityQueue:
    def __init__ (self):
        self.__data = list()
        self.__size = 0

    def is_empty (self):
        if self.__size == 0:
            return True
        else:
            return False

    def lenght (self):
        return print(f"El tamanio de la lista es : {self.__size}")

    def enqueue (self, prioridad, elem):
        posicion = 0
        for tripulante in self.__data:
            if prioridad >= tripulante [0]:
                posicion += 1
        if self.is_empty() == True or self.__size == posicion :
            self.__data.append((prioridad,elem))
            self.__size += 1
        else:
            self.__data.insert(posicion,(prioridad,elem))
            self.__size += 1

    def dequeue (self):
        self.__data.pop()
        self.__size -= 1

    def to_string (self):
        cadena = ""
        for elem in self.__data :
            cadena = cadena + " | "+ str(elem)
        cadena = cadena + " | "
        return cadena



class BoundedPriorityQueue :
    def __init__ (self,niveles):
        self.__data = [Queue() for x in range(niveles)]
        self.__size = 0

    def is_empty (self):
        return self.__size == 0

    def lenght (self):
        return print (f"El tamanio de la lista es : {self.__size}")

    def enqueue (self,prioridad,elem):
        if prioridad < len(self.__data) and prioridad >= 0 :
            self.__data[prioridad].enqueue(elem)
            self.__size += 1

    def dequeue(self):
        if not self.is_empty():
            for nivel in self.__data:
                if not nivel.is_empty():
                    self.__size-=1
                    return nivel.dequeue()

    def to_string(self):
        print("COLA:")
        for nivel in range (len(self.__data)):
            print (f"Nivel {nivel} --> {self.__data[nivel].to_string()}")
