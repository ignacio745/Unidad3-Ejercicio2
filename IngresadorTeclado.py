class IngresadorTeclado:
    __valor = None

    def __init__(self):
        self.__valor = None
    

    def inputInt(self, mensaje, mensajeError="El dato debe ser un entero, reingrese el valor: "):
        self.__valor = input(mensaje)
        band = True
        while band:
            try:
                self.__valor = int(self.__valor)
            except:
                self.__valor= input(mensajeError)
            else:
                band = False
        
        return self.__valor
    

    def inputFloat(self, mensaje, mensajeError="El dato debe ser un decimal con punto, reingrese el valor: "):
        self.__valor = input(mensaje)
        band = True
        while band:
            try:
                self.__valor = float(self.__valor)
            except:
                self.__valor= input(mensajeError)
            else:
                band = False
        
        return self.__valor