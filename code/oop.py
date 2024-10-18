class Auto:
    # Eigenschaften - Attribute
    # Konstruktor/Initializer -> versetzt ein Objekt in einen gültigen Ausgangszustand
    def __init__(self, marke, farbe, karosserieform, leistung):
        self.marke = marke
        self.farbe = farbe
        self.karosserieform = karosserieform
        self.leistung = leistung
        self.geschwindigkeit = 0


    # Funktionalitäten - Methoden
    def beschleunigen(self, faktor):
        self.geschwindigkeit += faktor
        print(f"Unser {self.marke} beschleunigt auf {self.geschwindigkeit} km/h.")

    def bremsen(self, faktor):
        self.geschwindigkeit -= faktor
        print(f"Unser {self.marke} bremst auf {self.geschwindigkeit} km/h ab.")

    def hupen(self):
        print(f"Honk Honk!")

    def __str__(self):
        return f"Das Auto {self.marke} ist {self.farbe}, ist ein {self.karosserieform}, hat {self.leistung} und fährt momentan {self.geschwindigkeit} km/h schnell."

# ---- Ende der Klassendefinition ----

bmw = Auto("BMW", "schwarz", "Kombi", "150 PS")
print(bmw.geschwindigkeit)
print(bmw.marke)
print(bmw.farbe)

bmw.beschleunigen(7)
bmw.beschleunigen(48)
print(bmw.geschwindigkeit)
bmw.bremsen(5)

citroen = Auto("Citroen", "weiss", "Coupe", "100 PS")
print(citroen.marke)
citroen.beschleunigen(30)
citroen.hupen()


print(f"{str(bmw)=}")
print(f"{str(citroen)=}")
citroen.beschleunigen(100)
print(f"{str(citroen)=}")
citroen.farbe = "gelb"
print(f"{str(citroen)=}")
