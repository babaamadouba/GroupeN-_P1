 # Exercice 1 : Gestion de stock (Variables, Saisie et Condition) 
# Demandez à l'utilisateur de saisir le stock initial de prooduits.
# Demandez le nombre de produits vendus aujourd'hui.
# Calculez et affichez le stock restant.
# Si le stock restant est strictement inférieur à 10, affichez le message :
# "Attention : stock faible, penser au  réapprovisionnement."


# Algorithme gestion_de_stock
      # variables: n, stock_initial, produits_vendus, stock_restant : integer
	  

stock_initial = int(input("Veuillez entrer le nombre de produits qui se trouve dans votre stock:"))
print(stock_initial)
          
produits_vendus = int(input("Veuillez entrer le nombre de produits contenus dans votre stock que vous avez vendus:"))
print(produits_vendus)

stock_restant = stock_initial - produits_vendus

if stock_restant < 10 :
 print(f"Attention : stock faible, penser au  réapprovisionnement car il vous reste {stock_restant} produits.")

else:          
 print(f"Ok, après calcul, nous pouvons vous dire qu'il vous reste {stock_restant } produits dans votre stock.")





