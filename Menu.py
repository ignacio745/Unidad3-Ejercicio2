from ManejadorFlores import ManejadorFlores
from ManejadorRamos import ManejadorRamos


class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.salir
                          }
    def opcion(self, unManejadorRamos, unManejadorFlores, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op in ('1', '2', '3'):
            func(unManejadorRamos, unManejadorFlores)
        else:
            func()
    def salir(self):
        print('Usted salio del programa')


    def opcion1(self, unManejadorRamos:ManejadorRamos, unManejadorFlores:ManejadorFlores):
        unManejadorRamos.crearyAgregarRamo(unManejadorFlores)


    def opcion2(self, unManejadorRamos:ManejadorRamos, unManejadorFlores:ManejadorFlores):
        unManejadorRamos.mostrarFloresMasPedidas(unManejadorFlores)
    
    def opcion3(self, unManejadorRamos:ManejadorRamos, unManejadorFlores:ManejadorFlores):
        unManejadorRamos.mostrarFloresVendidas(unManejadorFlores)


    def ejecutarMenu(self, unManejadorRamos:ManejadorRamos, unManejadorFlores:ManejadorFlores):
            opcion = "0"
            while opcion != "4":
                print("Ingrese la opcion deseada")
                print("[1] Agregar un Ramo")
                print("[2] Mostrar el nombre de las 5 flores mas pedidas en un tamaño de ramo")
                print("[3] Mostrar las flores vendidas en un tamaño de ramo")
                print("[4] Salir")
                opcion = input("--> ")  
                self.opcion(unManejadorRamos, unManejadorFlores, opcion)