# Shopsystem

# Was soll unser System leisten können?
# - [ ] Begrüssung / "Landing Page"
# - [ ] Navigation -> Auswahlmenü

#  - [ ] Bestellungvorgang abschliessen / zur Kasse gehen
#  - [ ] Warenkorb
#   - [ ] Gesamtpreis berechnen
# - [ ] Produktauswahl
#  - [ ] Preise
#  - [ ] Bestandsliste: Produkt noch vorhanden? Anzahl? Ausverkauft?
# - [ ] Namen

# Eventuell:
# - [ ] evtl. Login für Kunden
# - [ ] evtl. Kategorien für die unterschiedlichen Produkte
# - [ ] evtl. Rabatte


# Landing Page: Auswahl anzeigen
# - [x] Menü anzeigen
# - [x] Eingabe entgegenehmen (mit input())
# - [x] Eingabe prüfen
#  - [x] Prüfung nicht erfolgreich: Meldung ausgeben 
#   - [x]Menü erneut anzeigen
# - [ ] Eingabe ok: entpsrechende Funktionalität aufrufen
#  - [x] zuerst mit Platzhalter
#   - [ ] anzeigen, wo wir uns befinden: Startseite -> Produkte -> Kategorien -> T-Shirts
#   - [ ] Menü zur weiteren navigation mit der Möglichkeit, zurück zu gehen

# Funktionen (müssen vor dem Aufruf deklariert werden)
def display_product_categories():
    product_menu = """
    [1] Hosen
    [2] T-Shirts
    [3] Socken
    """
    while True:
        print(product_menu)
        user_input_product = input("Bitte eine Kategorie auswählen: ")

        # Prüfung des inputs
        if user_input_product.isdigit():
            user_input_product = int(user_input_product)
            if user_input_product > 0 and user_input_product <= 3:
                if user_input_product == 1:
                    print("Hosen")
                if user_input_product == 2:
                    print("T-Shirts")
                if user_input_product == 3:
                    print("Socken")
                break    # Schleife verlassen
            else:
                print("Falsche Eingabe")
        else:
            print("Bitte als Eingabe nur Ziffern von 1 bis 3 verwenden.")



# Logik

start_menu = """
[1] Produkte
[2] Warenkorb
[3] Programm beenden
"""
while True:
    # Auswahlmenü anzeigen
    print(start_menu)
    # Benutzereingabe entgegennehmen
    user_input = input("Wähle einen Menüpunkt: ")

    # Prüfung des inputs
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input > 0 and user_input <= 3:
            if user_input == 1:
                display_product_categories()
            if user_input == 2:
                print("Warenkorb")
            if user_input == 3:
                print("Programm beenden")
            break    # Schleife verlassen
        else:
            print("Falsche Eingabe")
    else:
        print("Bitte als Eingabe nur Ziffern von 1 bis 3 verwenden.")


