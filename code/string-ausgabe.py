# Ausgabe von Strings und Variablen in Python

name = "Gretl"
alter = 11
geburtsjahr = 2013

tierart = "Hund"
rasse = "Labrador"

# Ausgabe über mehrere Argumente, durch Komma getrennt
print("Der Hund heisst", name, "und ist", alter, "Jahre alt.")
print(name, " ist ein ", rasse, tierart, sep="")

# Ausgabe eines Strings mit der String-Konkatenation (+ Operator)
print(name + " ist ein " + rasse + tierart)        # + Konkatenations-Operator (Verketteung von Strings)
print(alter + geburtsjahr)    # + Additions-Operator (Verkettung von Integern)

# Vorsicht beim Mischen von Datentypen! Die Verkettung von Strings und Integern ist nicht möglich,
# wir müssen den Integer vorher in einen String casten (umwandeln)
print("Der Hund heisst " + name + " und ist " + str(alter) + " Jahre alt.")

