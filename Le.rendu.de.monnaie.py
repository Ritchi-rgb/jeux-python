#Un client doit payer un montant entier en euros et donne un billet de 50 €. Affichez comment lui rendre la
#monnaie avec le moins de billets et de pièces possible, parmi 20 €, 10 €, 5 €, 2 € et 1 €. N'affichez que les
#lignes utiles. Indice : // et % font tout le travail.

nombre_1 = int(input("Indiquer le montant à payer ? : "))
somme = 50 - nombre_1

if nombre_1 < 14:
    print(f"Rendu {somme} € :\n {somme // 20} billet(s) de 20 €\n {somme % 20 // 10} billet(s) de 10 €\n {somme % 10 // 5} billet(s) de 5 €\n {somme % 5 // 2} pièce(s) de 2 €")