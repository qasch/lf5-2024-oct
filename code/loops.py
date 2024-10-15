# While Loop

# Redundanter Code -> wollen wir immer vermeiden!
# Programmierkonzept: DRY -> Don't Repeat Yourself
# print("Jawoll")
# print("Jawoll")
# print("Jawoll")
# print("Jawoll")
# print("Jawoll")
# print("Jawoll")
# print("Jawoll")
# print("Jawoll")
# print("Jawoll")

# Eine while Schleife ist einer if-Bedingung sehr ähnlich:

#bedingung = True
# if bedingung:
#     print("Jawoll")

# EndlosLoop, hört nie auf
# while bedingung:
#     print("Jawoll")

# "Jawoll" 10x ausgeben
anzahl = 1
hoechstwert = 10
while anzahl <= hoechstwert:
    print("Jawoll")
    # anzahl = anzahl + 1    # anzahl bei jedem Schleifendurchlauf um 1 erhöhen (inkrementieren)
    anzahl += 1            # Kurzschreibweise für obigen Ausdruck

print("Schleife zu Ende. Anzahl:")
print(anzahl)

print()
print("-----------------------------")
print()

# While Schleife, die die Zahlen von 20 bis 10 in absteigender Reihenfolge ausgibt:
startwert = 20 
endwert = 10
while startwert >= endwert:
    print(startwert)
    startwert = startwert - 1     # Dekrement

print()
print("-----------------------------")
print()

# For Loop

# 10x "Jawoll" ausgeben
for count in range(10):
    print("Jawoll")

# Zahlen von 0 bis 9 ausgeben
for count in range(10):
    print(count)

# Zahlen von 10 bis 19 ausgeben
for count in range(10, 20):
    print(count)

# Zahlen von 20 bis 10 ausgeben
for count in range(20, 10):
    print(count)

# Zahlen von 10 bis 19 in 2er Schritten (steps) ausgeben
for count in range(10, 20, 2):
    print(count)

print()
print("---Loop mit break ---")
print()

# Schlüsselwort break
for count in range(100):
    print(count)
    if count == 20:
        print("Schlüsselwort break bei count == 20")
        break           # Schleife wird beendet

print("nach der Schleife")

print()
print("---Loop mit continue ---")
print()

# Schlüsselwort continue
for count in range(100):
    print("Punkte: ", count)
    if count < 80:
        continue           # 
    print("Ui, fast gewonnen")

print("Yeah, 100 Punkte - gewonnen!")

print()
print("--- for Loop mit String ---")
print("", end="\n")
text = "Die Sonne scheint"
for letter in text:
    print(letter, end="|")
print("nach dem loop")

print()
print("--- while Loop mit break ---")
print()
# Benutzer soll wiederholt eine Zahl eingeben können
# erst wenn die Zahl grösser ist als 10, soll die Meldung erscheinen:
# Zahl ist grösser als 10 und keine Eingabeaufforderung mehr erscheinen

# bewusst gebaute Endlosschleife
while True:
    eingabe = int(input("Bitte gib eine Zahl groesser als 10 ein: "))
    if eingabe > 10:
        print(f"Du hast {eingabe} eingegeben. {eingabe} ist groesser als 10. Glückwunsch!")
        break
    print(f"Du hast {eingabe} eingegeben. {eingabe} ist nicht groesser als 10. Versuche es erneut.")


