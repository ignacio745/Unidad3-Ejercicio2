from Ramo import Ramo
from typing import List
from IngresadorTeclado import IngresadorTeclado
from ManejadorFlores import ManejadorFlores
from Flor import Flor

class ManejadorRamos:
    __ramos = None
    __ingresador = None
    

    def __init__(self):
        self.__ramos:List[Ramo] = []
        self.__ingresador = IngresadorTeclado()
        self.__tamaños = ["chico", "mediano", "grande"]


    def agregarRamo(self, unRamo):
        if isinstance(unRamo, Ramo):
            self.__ramos.append(unRamo)
        else:
            print("[ERROR] No se puede agregar un objeto de la clase {0}".format(unRamo))


    def ingresarTamañoRamo(self) -> str:
        tamaño = self.__ingresador.inputInt("Ingrese el tamaño del ramo\n[1] Chico\n[2] Mediano\n[3] Grande\n--> ")
        while not 1<=tamaño<=3:
            print("Valor invalido, reintente")
            tamaño = self.__ingresador.inputInt("Ingrese el tamaño del ramo\n[1] Chico\n[2] Mediano\n[3] Grande\n--> ")
        tamaño = self.__tamaños[tamaño - 1]
        return tamaño


    def crearyAgregarRamo(self, unManejadorFlores:ManejadorFlores):
        tamaño = self.ingresarTamañoRamo()
        unRamo = Ramo(tamaño)
        print("Ingresa un numero de flor para agregar, 0 para finalizar: ")
        for unaFlor in unManejadorFlores:
            print("[{0}] {1} {2}".format(unaFlor.getNumero(), unaFlor.getNombre(), unaFlor.getColor()))
        numero = self.__ingresador.inputInt("--> ")
        while numero != 0:
            unaFlor = unManejadorFlores.getFlorPorNumero(numero)
            if isinstance(unaFlor, Flor):
                unRamo.agregarFlor(unaFlor)
                print("Flor agregada")
            numero = self.__ingresador.inputInt("--> ")
        self.agregarRamo(unRamo)
    

    def mostrarFloresMasPedidas(self, unManejadorFlores:ManejadorFlores):
        tamaño = self.ingresarTamañoRamo()
        contadores:List[int] = [0 for i in unManejadorFlores]
        for unRamo in self.__ramos:
            if unRamo.getTamaño() == tamaño:
                for unaFlor in unManejadorFlores:
                    contadores[unaFlor.getNumero()-1] += unRamo.getCantFloresNumero(unaFlor.getNumero())
        
        numerosMayores = []
        for i in range(5):
            mayor = 0
            numero = 0
            for j in range(len(contadores)):
                if contadores[j] > mayor:
                    mayor = contadores[j]
                    numero = j
            numerosMayores.append(numero+1)
            contadores[numero] = 0
        print("Las 5 flores mas pedidas en el ramo {0} son:".format(tamaño))
        print("{0:<20}{1:<20}{2}".format("Numero", "Nombre", "Color"))
        for numero in numerosMayores:
            unaFlor = unManejadorFlores.getFlorPorNumero(numero)
            print("{0:<20}{1:<20}{2}".format(unaFlor.getNumero(), unaFlor.getNombre(), unaFlor.getColor()))


    def mostrarFloresVendidas(self, unManejadorFlores:ManejadorFlores):
        flores = ManejadorFlores()
        
        tamaño = self.ingresarTamañoRamo()
        
        for unaFlor in unManejadorFlores:
            i = 0
            while i < len(self.__ramos) and flores.buscarFlorPorNumero(unaFlor.getNumero()) == -1:
                if self.__ramos[i].getTamaño() == tamaño and self.__ramos[i].checkFlorNumero(unaFlor.getNumero()):
                    flores.agregarFlor(unaFlor)
                i += 1
        print("Flores vendidas en ramo {0}".format(tamaño))
        print("{0:<20}{1:20}{2}".format("Numero", "Nombre", "Color"))
        for unaFlor in flores:
            print("{0:<20}{1:<20}{2}".format(unaFlor.getNumero(), unaFlor.getNombre(), unaFlor.getColor()))
        