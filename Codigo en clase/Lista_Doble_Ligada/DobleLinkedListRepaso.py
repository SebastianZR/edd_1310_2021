class NodoDoble :
    def __init__(self,value,anterior = None, siguiente= None):
        self.data = value
        self.next = siguiente
        self.prev = anterior

class DoubleLinkedList :
    def __init__(self):
        self.__head = NodoDoble(None)
        self.__tail = NodoDoble(None)
        self.__size = 0

    def get_size (self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def append (self,value):

        if self.is_empty():
            nuevo = NodoDoble (value)
            self.__head = nuevo
            self.__tail = nuevo

        else :
            nuevo = NodoDoble (value ,  self.__tail ,None)
            self.__tail.next = nuevo
            self.__tail = nuevo
        self.__size += 1

    def transversal (self):
        curr_node = self.__head
        while curr_node != None:
            print (f"<-------{curr_node.data}------>" , end = "")
            curr_node = curr_node.next
        print ("")

    def reversetransversal (self):
        curr_node = self.__tail
        while curr_node != None:
            print (f"<-------{curr_node.data}------>" , end = "")
            curr_node = curr_node.prev
        print ("")

    def removefromhead (self,value):
        curr_node = self.__head
        if self.__head.data == value:
            self.__head = self.__head.next
            self.__head.prev = None
            self.__size +=1
        else:
            while curr_node != value and curr_node != None:
                curr_node = curr_node.next
            if curr_node.data == value :
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev
                self.__size -= 1
