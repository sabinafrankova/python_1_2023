class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return "Potvrzuji zapůjčení vozidla"
        else:
            return "Vozidlo není k dispozici"

    def get_info(self):
        return f"Registrační značka: {self.registracni_znacka}, značka a typ vozidla: {self.typ_vozidla}"

auto_p = Auto("4A2 3030", "Peugeot 403 Cabrio", 47534)
auto_s = Auto("1P3 4747", "Škoda Octavia", 41234)

vyber = input("Zadej značku vozidla (Peugeot/Škoda): ")

if vyber.lower() == "peugeot":
    print(auto_p.get_info())
    vysledek = auto_p.pujc_auto()
    print(vysledek)
elif vyber.lower() == "škoda":
    print(auto_s.get_info())
    vysledek = auto_s.pujc_auto()
    print(vysledek)
else:
    print("Taková značka není k dispozici")


#test
if vyber.lower() == "peugeot":
    print("Pokus o opětovné zapůjčení vozidla:")
    vysledek = auto_p.pujc_auto()
    print(vysledek)
else:
    print("Pokus o opětovné zapůjčení vozidla:")
    vysledek = auto_s.pujc_auto()
    print(vysledek)