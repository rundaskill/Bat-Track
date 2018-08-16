from MyScripts import library
from MyScripts import ToDraw
import os




def ImgDirectorio():

    rutafull=library.CrearArchivo()
    library.CrearCodigoBat(rutafull,'Pictures','*.jpg,*.jpeg,*.png',True,True)

def DocDirectorio():
    rutafull=library.CrearArchivo()
    library.CrearCodigoBat(rutafull,'Documents','*.pdf,*.docx,*.xlsx,*.pptx,*.txt',True,True)

def AllDirectorio():
    """
    rutafull = library.CrearArchivo()
    library.CrearCodigoBat(rutafull, 'Pictures', '*.jpg,*.jpeg,*.png', True, False)
    library.CrearCodigoBat(rutafull, 'Documents', '*.pdf,*.docx,*.xlsx,*.txt', False, True)"""
def Menu():
    os.system('cls')

    ToDraw.dibujo()
    print (chr(27)+"[1;37m"+"select an option")
    print ("\t1 copy images .Bat")
    print ("\t2 copy documents .Bat")
    print ("\t3 copy all .Bat")
    print ("\t99 Exit")


while True:

    Menu()
    opcionMenu = input("enter the number >> ")

    if opcionMenu == '1':
         ImgDirectorio()
    elif opcionMenu == '2':
         DocDirectorio()
    elif opcionMenu == '3':
         AllDirectorio()
    elif opcionMenu == '99':
        break
    else:
         input ("please select an option of 1 to 3 ...")



