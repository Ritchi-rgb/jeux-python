#La place coûte 11 €. Moins de 14 ans : 6 €. Étudiants de moins de 26 ans : 8 €. 65 ans et plus : 8 €. 
# Demandez l'âge, puis demandez « Êtes-vous étudiant (o/n) ? » seulement si c'est utile, et affichez le prix.

nombre_1 = int(input("Quel est votre âge ? : "))

if nombre_1 < 14:
    print("Le prix de la place est de 6 €.")
elif nombre_1 < 26:
    print("Le prix de la place est de 8 €.")
elif nombre_1 >= 65:
        print("Le prix de la place est de 8 €.")
else:
        print("Le prix de la place est de 11 €.")