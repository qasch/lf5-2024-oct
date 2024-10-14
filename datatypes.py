# Datenypen in Python

## String - Zeichenkette
my_string = "hallo"

## Integer - Ganzzahl
my_int = 42        # Zuweisung des Werts 42 an die Variable my_int
alter = 35

## Float - Gleitkommazahl
my_float = 3.14    # Wichtig: der Punkt ist der Dezimaltrenner, nicht das Komma

## Boolean - Wahrheitswert (nur True oder False)
my_boolean = False

# ----------------------------------
# Eine List kann mehr als einen Wert aufnehmen, z.B. Einkaufsliste
my_list = ["Butter", "Käse", "Brot", "Bananen", "Eier"]

# Ein Tuple ist ähnlich wie eine List, die Werte können aber nicht mehr verändert werden 
my_tuple = (23.234324, 987987.9283794)

# Ein Set ist ähnlich wie eine list, Werte können aber nur einmal vorkommen
my_set = {1, 2, 3, 4, 4, 4, 4, 4, 4, 4}

# Eine Art Wörterbuch (Dictionary), bei dem einem Schlüssel ein bestimmter Wert zugewiesen ist
my_dict = {"name": "gretl", "alter": "11", "hobbies": "essen"}







# Ausgabe der Inhalte der Variablen
print("my_string:", my_string)
print("my_int:", my_int)
print("alter:", alter)
print("my_int, alter:", my_int, alter)  # Ausgabe beider Variablen (in einer Zeile)
print("my_float:", my_float)
print("my_boolean:", my_boolean)
print("my_list:", my_list)




print(my_dict)
print(my_dict["alter"])

print(my_set)