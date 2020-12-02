from Array2d impor Array2D


class LaberintoADT :
    def __init__(self,rens,cols,pasillos):
        self.__laberinto = Array2D(rens , cols , '1')
        for pasillo in pasillos :
            self.___laberinto.set_item(pasillo[0] , pasillo[1] , '0')
    def to_string (self):
        self.__laberinto.to_string()
    
