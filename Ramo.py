from typing import List
from Flor import Flor
from ManejadorFlores import ManejadorFlores

class Ramo:
    __tamaño = ""
    __flores = None

    def __init__(self, tamaño:str):
        self.__tamaño = tamaño
        self.__flores = ManejadorFlores()
    
    def agregarFlor(self, unaFlor:Flor):
        self.__flores.agregarFlor(unaFlor)
    
    def getTamaño(self):
        return self.__tamaño
    
    def getCantFloresNumero(self, numero) ->int:
        cont = 0
        for unaFlor in self.__flores:
            if unaFlor.getNumero() == numero:
                cont += 1
        return cont
    
    def checkFlorNumero(self, numero) -> bool:
        return self.__flores.checkFlorNumero(numero)