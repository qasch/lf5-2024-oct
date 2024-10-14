# Verzweiungen / if (else) Statements

# if prüft, ob ein Ausdruck True oder False ist,
# nur wenn True werden die Anweisungen im if-Block ausgegeben:
# if 10 > 2:  # True
#     print("10 ist grösser als 2")

# if 1 > 2:  # False
#     print("10 ist grösser als 2")

# print("Ende des Programms")


# zahl1 = 20
# zahl2 = 10

# if zahl1 > zahl2:
#     print(zahl1, "ist grösser als", zahl2)
# else:
#     print(zahl1, "ist kleiner als", zahl2)

# print("Nach der if-Anweisung")



zahl1 = "hallo"
zahl2 = 10

if zahl1 == zahl2:
    print(zahl1, "ist gleich", zahl2)
elif zahl1 > zahl2:
    print(zahl1, "ist grösser als", zahl2)
elif zahl1 < zahl2:
    print(zahl1, "ist kleiner als", zahl2)
else:
    print("Irgendwas stimmt nicht...")

print("Nach der if-Anweisung")