# Écrire un algorithme qui demande 5 nombres à l'utilisateur, 
# et les afficher dans l’ordre croissant.


def Ordre_Croissant() :
    liste_nombre =[]
    
    for i in range(1,6):
        nombre = int(input("Veuillez entrer un nombre :"))
        liste_nombre.append(nombre)

    for i in range(len(liste_nombre)) :
        
        for j in range(i+1,len(liste_nombre)) :
           
            if liste_nombre[i] > liste_nombre[j] :
                   
               liste_nombre[i],liste_nombre[j] = liste_nombre[j],liste_nombre[i]

    print(f"La liste trie des 5 nombres est: {liste_nombre}")

print("Debut du programme principal")
Ordre_Croissant()
print("Fin du programme")
           




