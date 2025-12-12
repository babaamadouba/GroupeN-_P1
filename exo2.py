# Exercice 2 : Fusionner deux listes (Création de listes) 🤝
# Demandez 3 nombres à l’utilisateur pour constituer une première liste (Liste A).
# Demandez 3 autres nombres à l’utilisateur pour constituer une deuxième liste (Liste B).
# Créez une troisième liste (Liste C) qui contient tous les éléments de la Liste A suivis de tous les éléments de la Liste B.
# Affichez la Liste C..

# Algorithme fusion_de_liste

NB_ELEMENTS = 3
liste_a = [] # Liste A (Tableau) pour stocker les nombres de la première liste
liste_b = [] # Liste B (Tableau) pour stocker les nombres de la deuxième liste


try:
    print("--- Remplissage de la LISTE A ---")
    # 1. Saisie des nombres et remplissage du tableau de la première liste
    for i in range(1, NB_ELEMENTS + 1):
       nombre_a = float(input("Veuillez entre les  nombres à stocker sur  la première liste : "))
       liste_a.append(nombre_a)
   
    print("\n--- Remplissage de la LISTE B ---")
    # 2. Saisie des nombres et remplissage du tableau de la deuxième liste
    for i in range(1, 4):
        nombre_b= float(input("Veuillez entre les  nombres à stocker sur  la deuxième liste : "))
        liste_b.append(nombre_b)
        
    # 3. Création et Affichage d'une troisième liste
        liste_c = liste_a + liste_b

        print(f"\n Liste A : {liste_a}")
        print(f"Liste B : {liste_b}")
        print(f"Les nombres qui constituent la liste C (Fusion) sont: {liste_c}")
    
   

except ValueError:
    print("Erreur de format : Veuillez saisir des valeurs numériques.")