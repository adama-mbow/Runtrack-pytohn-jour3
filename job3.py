#Créez une fonction qui affiche tous les nombres de 0 à 100 compris SAUF 26, 37, 88
def nombre():
    for i in range(101):
        if i == 26 or i == 37 or i == 88:
            print("-")

        else:
            print(i)

print(nombre())
    
