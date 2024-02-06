import UserFunctions
import AdminFunctions


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
            print("3. Eliminar pel·líca")
            print("4. Eliminar usuari")
            print("5. Tancar l'aplicació")
            opcio = int(input("Introdueix una opció -> "))

            if opcio == 1:
                AdminFunctions.crearPeli()
                pass
            elif opcio == 2:
                AdminFunctions.consultarCommentsUsuari()
                pass
            elif opcio == 3:
                AdminFunctions.eliminarPeli()
                pass
            elif opcio == 4:
                AdminFunctions.eliminarUser()
                pass
            elif opcio == 5:
                print("Fins prompte!!")
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
            print("6. Tancar l'aplicació")
            opcio = int(input("\n Introdueix una opció -> "))

            if opcio == 1:
                UserFunctions.mostrarInfoPeli()
                pass
            elif opcio == 2:
                UserFunctions.consultarPelisGenere()
                pass
            elif opcio == 3:
                UserFunctions.consultarActorsPeli()
                pass
            elif opcio == 4:
                UserFunctions.consultarCommentsPeli()
                pass
            elif opcio == 5:
                UserFunctions.crearUsuari()
                pass
            elif opcio == 6:
                print("Fins prompte!!")
                break
            else:
                print("La opció que has introduit es incorrecta, torna a probar")



    
menu()