#Demandez deux nombres entiers, puis affichez leur somme, leur différence, leur produit (multiplication), leur quotient (leur division)
# (avec / ), le quotient entier (//) et le reste (modulo). Une ligne par opération, sous la forme 17 // 5 = 3 .

nombre_1 = int(input("Donner moi un 1er nombre entier : "))
nombre_2 = int(input("Donner moi un 2eme nombre entier : "))

somme = nombre_1 + nombre_2
difference = nombre_1 - nombre_2
multiplication = nombre_1 * nombre_2
quotient = nombre_1 / nombre_2
quotient_entier = nombre_1 // nombre_2
reste = nombre_1 % nombre_2

print(f"Bonjour la somme est : {somme}")
print(f"Bonjour la différence est : {difference}")
print(f"Bonjour la multiplication est : {multiplication}")
print(f"Bonjour le quotient est : {quotient}")
print(f"Bonjour le quotient_entier est : {quotient_entier}")
print(f"Bonjour le reste est : {reste} ")
