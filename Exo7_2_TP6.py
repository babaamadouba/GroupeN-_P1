#Le mot de passe correct = "1234a"
#L’utilisateur a 5 tentatives maximum.
#Après 5 tentatives échouées,  afficher "Compte bloqué".

def Tentative (nbr_tentative, password_correct ) :
    i = 0
    while i < nbr_tentative :
        print("Veuillez saisir un mot de passe valide")
        password = input("Entrer voter mot de passe ")

        if password != password_correct :
            print(" vous avez saisi un mot de passe invalide")    
            if i < nbr_tentative +1 :
             print(f"Il vous reste {nbr_tentative -(1+i)} tentatives")

        else:
         print("Bravo vous avez choisi un mot valide")
       
         break
        i = i +1
    if password != password_correct :
     print("Acces refuse : compte bloque")

print("Debut du progamme principal")
Tentative(5,"1234567")
print("Fin du programme")


