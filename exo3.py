# Exercice 3 : Filtrer les éléments négatifs d'une liste (Boucle et Condition)
# Demandez à l'utilisateur de saisir 10 nombres (positifs ou négatifs).
# Créez une nouvelle liste qui contient uniquement les nombres supérieurs ou égaux à 0 (nombres non négatifs).
# Affichez la nouvelle liste.

# Algorithme filtre_de_liste

NB_ELEMENTS = 10

 # Liste A (pour stocker TOUTES les entrées de l'utilisateur)
liste_complete = []
# Liste P (pour stocker les nombres non négatifs)
liste_p = [] 

try:
    print("--- Saisie des 10 nombres ---")
    
    # 1. Saisie des 10 nombres et stockage dans la liste_complete
    for i in range(NB_ELEMENTS):
      
       nombre_saisi = float(input(f"Entrez le nombre {i+1} : "))
       liste_complete.append(nombre_saisi) # Ajout du nombre à la liste

    print("\n--- Filtrage des nombres non négatifs ---")
    
    # 2. Itération sur la liste stockée pour appliquer le filtre
   
    for element in liste_complete:
        
        if element >= 0: 
            # Si la condition est vraie, on ajoute l'élément à la liste filtrée
            liste_p.append(element) 
     
    # 3. Affichage de la liste finale (DOIT ÊTRE APRÈS la boucle de filtrage)
    print(f"Les nombres positifs (>= 0) de la liste d'origine sont: {liste_p}")
    
except ValueError:
   
    print("Erreur de format : Veuillez saisir des valeurs numériques.")