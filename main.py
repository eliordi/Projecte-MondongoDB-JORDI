











def menu():

    print("\n---------------------")
    print("| PROJECTE MONGO DB |")
    print("|    -JORDFLIX-     |")
    print("---------------------")

    usuari = input("Introdueix el nom d'usuari: ")

    if usuari == "admin":
        
        while(True):
            print("\nMENÚ ADMIN: ")
            print("1. Crear una pel·lícula")
            print("2. Consultar tots els comentaris d'un usuari")
            print("3. Eliminar pel·lícules")
            print("4. Eliminar comentaris")
            print("5. Eliminar usuaris")
            print("6. Per a tancar l'aplicació")
            opcio = int(input("Introdueix una opció -> "))

            if opcio == 1:
                pass
            elif opcio == 2:
                pass
            elif opcio == 3:
                pass
            elif opcio == 4:
                pass
            elif opcio == 5:
                pass
            elif opcio == 6:
                break
            else:
                print("La opció que has introduit es incorrecta, torna a probar")

    else:
        
        while(True):

            print("\nMENÚ USUARI: ")
            print("1. Mostrar tota l'informació d'una pel·lícula")
            print("2. Consultar totes les pel·lícula d'un gènere")
            print("3. Consultar tots els actors d'una pelpel·lículaícula")
            print("4. Consultar els comentaris d'una pel·lícula")
            print("5. Crear un usuari")
            print("6. Fer un comentari a alguna pel·lícula (Antes has de crear un usuari)")
            print("7. Modificar un comentari (Antes has de crear un usuari i fer un comentari)")
            print("8. Per a tancar l'aplicació")
            opcio = int(input("Introdueix una opció -> "))

            if opcio == 1:
                pass
            elif opcio == 2:
                pass
            elif opcio == 3:
                pass
            elif opcio == 4:
                pass
            elif opcio == 5:
                pass
            elif opcio == 6:
                pass
            elif opcio == 7:
                pass
            elif opcio == 8:
                break
            else:
                print("La opció que has introduit es incorrecta, torna a probar")


    
    
    
menu()