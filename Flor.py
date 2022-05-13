class Flor:
    __numero = None
    __nombre = ""
    __color = ""
    __descripcion = ""

    def __init__(self, numero:int, nombre:str, color:str, descripcion:str):
        self.__numero = numero
        self.__nombre = nombre
        self.__color = color
        self.__descripcion = descripcion
    

    def getNumero(self) ->int:
        return self.__numero
    
    def getNombre(self) ->str:
        return self.__nombre
    
    def getColor(self) ->str:
        return self.__color
    
    def getDescripcion(self) ->str:
        return self.__descripcion