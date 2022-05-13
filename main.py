from ManejadorFlores import ManejadorFlores
from ManejadorRamos import ManejadorRamos
from Menu import Menu
import os

if __name__=='__main__':
    os.system("clear")
    unManejadorRamos = ManejadorRamos()
    unManejadorFlores = ManejadorFlores()
    unMenu = Menu()
    unManejadorFlores.cargarCSV("flores.csv")
    unMenu.ejecutarMenu(unManejadorRamos, unManejadorFlores)