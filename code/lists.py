# Lists

## Variablen (können exakt einen Wert aufnehmen)
zahl = 7
print("zahl=" + str(zahl))      # Ausgabe zahl=7
print(f"{zahl}")               # Ausgabe 7
print(f"{zahl=}")              # Ausgabe zahl=7


## Lists können beliebig viele Werte aufnehmen
my_list = []    # Erstellen einer leeren List

#  index: 0  1  2  3   4
zahlen = [3, 1, 5, 9, 187]     # mehrere Elemente durch Komma getrennt

print(f"{my_list=}")
print(f"{zahlen=}")

# Ausgabe aller Elemente der List zahlen:
print("Ausgabe aller Elemente der List zahlen:")
for element in zahlen:
    print(element)

print()
print("Ausgabe einzelner Elemente der List zahlen:")
print(f"{zahlen[0]=}")     # einzelne Elemente können über ihren Index angesprochen werden
print(f"{zahlen[3]=}")     # Vorsicht: das 1. Element steht am Index 0, wir beginnen immer bei 0 mit zählen
print(f"{zahlen[4]=}")
# print(f"{zahlen[5]=}")   # führt zu einem "list index out of range" Fehler,
                           # da der angegebenen Index nicht existiert

print("---------------")

# Lists können verschiedene (und auch unterschiedliche) Datentypen aufnehmen
strings = ["Hund", "Katze", "Kanarienvogel"]    # List aus Strings
mixed_list = [42, "Braunbär", 3.14, True]       # List mit unterschiedlichen Datentypen

print("Ausgabe der Datentypen der einzelnen Elemente:")
for element in mixed_list:
    print(type(element))

print()
print("--- Elemente ändern ---")
print()
print(f"{mixed_list[0]=}")
mixed_list[0] = "foo"
print(f"{mixed_list[0]=}")
