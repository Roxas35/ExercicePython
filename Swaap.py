# Exrecice 2


# On crée les deux nombres à saisir dans le terminal.
a = int(input("Entrez un nombre : "))

b = int(input("Entrez un nombre : "))


# On crée les différents swap des entiers
temp_1 = a
a = b
b = temp_1

# On affiche la phrase si dessous en prenant en compte les nombres précédenments entrées dans le terminal.
print("La valeur de a après le swap: ", a)
print("La valeur de b après le swap: ", b)

