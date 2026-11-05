#L'ordinateur pense à un nombre entre 1 et 100. Vous proposez, il répond « C'est plus » ou « C'est moins », jusqu'à
#ce que vous trouviez.
#secret = 42
import random 
secret = random.randint(1, 100) # un entier au hasard entre 1 et 100, inclus
proposition = 0
coups = 0

print(f"Le nombre mystère est : {secret}")

while proposition != secret and coups < 3:
    proposition = int(input("Devinez le nombre mystère entre 1 et 100 : "))
    coups += 1  
    print(f"Votre proposition : {proposition}")
    if proposition == secret:
        print("C'est gagné")
        print(f"Bravo, trouvé en {coups} coups !")
    elif proposition < secret:
        print("C'est plus")
    elif proposition > secret:
        print("C'est moins")
    if coups == 3 and proposition != secret:
        print(f"Désolé, vous avez perdu, le nombre secret était {secret} !")




#proposition = 0
#while proposition != secret:
# demander la proposition
# dire si c'est plus ou si c'est moins
#print("Bravo, c'est gagné !")

#nombre_1 = int(input("Quel est votre âge ? : "))

#if nombre_1 < 14:
#    print("Le prix de la place est de 6 €.")
#elif nombre_1 < 26:
#    print("Le prix de la place est de 8 €.")
#elif nombre_1 >= 65:
#        print("Le prix de la place est de 8 €.")
#else:
#        print("Le prix de la place est de 11 €.")

