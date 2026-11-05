#Une année est bissextile si elle est divisible par 4, sauf si elle est divisible par 100, sauf si elle est divisible par
#400. Demandez une année et dites si elle est bissextile. À tester : 2024 (oui), 2026 (non), 1900 (non), 2000 (oui).

annee = int(input("Entrer l'année : "))
if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    print(f"L'année {annee} est bissextile.")
else:
    print(f"L'année {annee} n'est pas bissextile.")