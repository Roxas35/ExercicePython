# Exercice 3


# On crée les trois entier à saisir dans le terminal.

a = int(input("Entrez un nombre : "))

b = int(input("Entrez un nombre : "))

c = int(input("Entrez un nombre : "))

# On crée un condition if pour comparer les trois valeurs saisis
if a > b and a > c:
    {
        print("le plus grand nombre est : ", a)
    }
elif b > c: 
    {
        print("le plus grand nombre est : ", b)
    }
else:
    {
        print("le plus grand nombre est : ", c)
    }
