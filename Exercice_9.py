#À partir d'une liste de 5 nombres (que vous pouvez définir ou demander à l'utilisateur), 
# affichez : la somme, la moyenne, le maximum et le minimum, en utilisant les fonctions intégrées de Python.

list = []
for i in range(1,6) :
    Nombre = int(input(f"Veuillez entrer le nombre{i}"))
    list.append(Nombre)
for i in list :
    Somme = sum(list)
    Moyenne = Somme/len(list)
    Maximum = max(list)
    Minimum = min(list)  

print(f"Voici la somme {sum()}")
print(f"Voici la moyenne {Moyenne}" )
print(f"Voici le maximum {max()}" )  
print(f"Voici le minimum {min()}" )