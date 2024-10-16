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

# Elemente einer bestehenden List hinzufügen:
shopping_list = ["Brot", "Käse", "Eier", "Butter"]
# shopping_list[4] = "Milch"     # geht so nicht, immer wenn wir einen nicht existierenden
                                 # Index referenzieren, erhalten wir den "index out of range" Fehler

# List Methoden
# Lists haben Methoden (-> Name für Funtionen in der Objektorientierten Programmierung)
# Methoden können im Unterschied zu Funktionen bzw. Builtins nicht einfach so aufgerufen werden (wie z.B. print()), 
# sondern brauchen ein Objekt, welches sie über die sog. "Punkt-Notation" aufrufen können:
#   print()           -> Funktion/Builtin
#   objekt.methode()  -> Methode

print(f"{shopping_list=}")
shopping_list.append("Milch")   # die Methode append() fügt ein neues Element ans Ende der list an
print(f"{shopping_list=}")

## List Slicing
print("--- List Slicing ---")
print(shopping_list[2:])
print(shopping_list[2:4])
print()



# Strings sind auch Objekte und haben ebenso Methoden, die über die Punkt-Notation aufgerufen werden können:
print("--- Strings sind ähnlich wie Lists: ---")
text = "hallo"
print(text)
print(text.capitalize())
print(text.upper())
print(text.count("l"))


print()
print("--- Aufgabe Vokale finden mit einer list: ---")

# vokale = "aeiou"
vokale = ["a", "e", "i", "o", "u"]
satz = "HAllo du"

# ohne Loop, vokale einzeln abfragen:
# if "a" in satz:
#     print("ja")
# if "e" in satz:
#     print("ja")

# wie oben, nur mit loop:
count = 0
for character in vokale:
    if character in satz:
        print(f"{character} ist in satz")
        count += 1

print(f"Anzahl Vokale {count}")

 



