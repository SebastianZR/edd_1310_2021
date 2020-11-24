class Array2D:

    def __init__(self,rows, cols, value):
        self.__cols = cols
        self.__rows = rows
        self.__array=[[value for x in range(self.__cols)] for y in range(self.__rows)]

    def to_string(self):
        [print("---",end="") for x in range(self.__cols)]
        print("")
        for ren in self.__array:
            print(ren)
        [print("---",end="") for x in range(self.__cols)]
        print("")

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def get_item(self,row,col):
        return self.__array[row][col]

    def set_item( self , row , col , valor ):
        self.__array[row][col]=valor

    def clearing(self, valor=0):
        for ren in range(self.__rows):
            for col in range(self.__cols):
                self.__array[ren][col]=valor

class JuegoDeLaVida:
    CELULA_VIVA = 1
    CELULA_MUERTA = 0 

    def __init__ (self,rens,cols,generaciones,poblacion):
        self.largo = cols
        self.alto = rens
        self.grid = Array2D(self.alto,self.largo, 0 )
        self.grid.clearing (self.CELULA_MUERTA)
        self.generaciones = generaciones

        for celula in poblacion :
            self.grid.set_item(celula[0],celula [1],self.CELULA_VIVA)
    #Método Grid, colorea la matriz
    def imprime_grid (self):
        for r in range (self.grid.get_num_rows()):
            for c in range (self.grid.get_num_cols()):
                if self.grid.get_item(r,c) == 0 :
                    print("░░",end="")
                else :
                    print("▓▓",end="")
            print ("")
    def get_num_rows(self):
        return self.__rows
    def get_num_cols(self):
        return self.__cols
    def set_celula_muerta (self,row,col):
        self.grid.set_item(row,col,self.CELULA_MUERTA)
    def set_celula_viva (self,row,col):
        self.grid.set_item(row,col,self.CELULA_VIVA)
    def get_is_viva (self,row,col):
        if self.grid.get_item(row,col)==1:
            return True
    def get_is_muerta (self,row,col):
        if self.grid.get_item(row,col)==0:
            return False
    def get_numero_vecinos_vivos (self,row,col):
        limites = [row-1,row+1,col-1,col+1]
        vivos = 0 
        limites = self.__ajusta_limites__(limites)
        if row >= 0 and row <= self.alto-1 and col >= 0 and col <= self.largo -1:
            for r in range (limites [0],limites [1]+1):
                for c in range (limites [2],limites [3]+1):
                    if r == row and c == col:
                        continue
                    else :
                        if self.grid.get_item(r,c) == self.CELULA_VIVA:
                            vivos += 1
        else :
             print ("Coordenada de la celula esta fuera de grid ")
        return vivos 
    def configura_generacion (self,nueva_poblacion):
        self.grid.clearing()
        for celula in nueva_poblacion :
            self.grid.set_item(celula[0],celula [1],self.CELULA_VIVA)

celulas = [[1,2],[2,1],[2,2],[2,3]]
jueggo = JuegoDeLaVida(6,8,6)

 

