#Demandez une température en degrés Celsius (elle peut être à virgule : float ), et affichez-la en Fahrenheit,
#avec une décimale. La formule : F = C × 9 / 5 + 32 . Vérifiez : 100 °C font 212 °F, et 37,5 °C font 99,5 °F.

nombre_1 = float(input("Donnez moi une température en degrés Celsius : "))

print(f"La température en degré Fahrenheit est : {nombre_1 * 9 / 5 + 32} °F")
