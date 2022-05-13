import csv
import numpy as np
from Flor import Flor

class ManejadorFlores:
    __cantidad = 0
    __tamaño = 4
    __incremento = 4
    __flores = None
    __actual = 0
    
    def __init__(self):
        self.__cantidad = 0
        self.__tamaño = 4
        self.__incremento = 4
        self.__flores = np.empty(4, dtype=Flor)
        self.__actual = 0
    

    def agregarFlor(self, unaFlor):
        if isinstance(unaFlor, Flor):
            if self.__tamaño == self.__cantidad:
                self.__tamaño += self.__incremento
                self.__flores.resize(self.__tamaño)
            self.__flores[self.__cantidad] = unaFlor
            self.__cantidad += 1
        else:
            print("[ERROR] No se puede agregar un objeto del tipo {0}".format(type(unaFlor)))
    

    def cargarCSV(self, nombreArchivo):
        archivo = open(nombreArchivo)
        reader = csv.reader(archivo, delimiter=";")
        cont = 0
        for fila in reader:
            cont += 1
            try:
                unaFlor = Flor(int(fila[0]), fila[1], fila[2], fila[3])
            except:
                print("[ERROR] No se pudo cargar la flor de la fila {0}".format(cont))
            else:
                self.agregarFlor(unaFlor)
        archivo.close()
    

    def buscarFlorPorNumero(self, numero:int) -> int:
        i = 0
        while i < self.__cantidad and self.__flores[i].getNumero() != numero:
            i += 1
        if i == self.__cantidad:
            i = -1
        return i

    def getFlorPorNumero(self, numero:int) -> Flor:
        unaFlor = None
        indice = self.buscarFlorPorNumero(numero)
        if indice == -1:
            print("[ERROR] No se encontro la flor")
        else:
            unaFlor = self.__flores[indice]
        return unaFlor
    
    
    def contarFlorNombre(self, nombre:str) ->int:
        cont = 0
        for i in range(self.__cantidad):
            if self.__flores[i].getNombre() == nombre:
                cont += 1
        return cont
    
    def checkFlorNumero(self, numero:int) -> bool:
        return self.buscarFlorPorNumero(numero) != -1



    def __iter__(self):
        self.__actual = 0
        return self

    def __next__(self) ->Flor:
        if self.__actual == self.__cantidad:
            raise StopIteration
        else:
            unaFlor = self.__flores[self.__actual]
            self.__actual += 1
            return unaFlor