Agenda = dict ()

print('Agenda Electonica')

print('Opcion 1: Contactos')
print('Opcion 2: Agregar nuevo contacto')
print('Opcion 3: Modificar contacto')
print('Opcion 4: Eliminar contacto')
print('Opcion 5: Buscar contacto')
print('Opcion 6: Salir')
print('************************************')


    
while True:
    seleccion = int(input('Seleccione una opcion: '))
    if seleccion == 6:
        break
    
    
    elif seleccion == 1:
        for i in Agenda:
             print(Agenda[i])
    
    
    elif seleccion == 2:
        nombre = input('Nombre: ')
        apellido =input('Apellido: ')
        mail = input('Mail: ')
        tel = int(input('Telefono: '))
        dir = input('Direccion: ')
        Agenda["Nombre"] = nombre
        Agenda["Apellido"] = apellido
        Agenda["Mail"] = mail
        Agenda["Telefono"] = tel
        Agenda["Direccion"] = dir

        if Agenda.get(tel) == None:
            print(Agenda)
        else:
            print('El contacto ya existe')    
            
    elif seleccion == 3:
        nombre = input('Ingrese el contacto a modificar: ')
        if Agenda.get(nombre) == None:
            print('Contacto inexistente, ingrese nuevo contacto a modificar: ')
        else:
            while True:
                print('1 Mail:')
                print('2 Telefono:')
                print('3 Direccion:')

                if seleccion == 1:
                    mail = input('Mail: ')
                    Agenda["Mail"] = mail
                if seleccion == 2:
                    tel = int(input('Telefono: '))
                    Agenda["Telefono"] = tel
                if seleccion == 3:
                    dir = input('Direccion: ')
                    Agenda["Direccion"] = dir

        
    elif seleccion == 4:
        nombre = input('Escriba el nombre del contacto que desea eliminar: ')
        if Agenda.get(nombre) == None:
            print('Contacto inexsitente')
        else:
            Agenda.pop(nombre)
            print(Agenda)
    
   
    elif seleccion == 5:
        nombre = input('Ingrese el contacto a buscar: ')
        for i in Agenda.keys():
            print(Agenda[i])


    else:
        print('Opcion incorrecta')






