sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

def prodej_soucastky():
    kod_soucastky = input("Zadejte kód součástky: ")
    
    if kod_soucastky not in sklad:
        print("Tato součástka není skladem.")
    else:
        pozadovane_mnozstvi = int(input(f"Kolik kusů součástky {kod_soucastky} si přejete koupit? "))
        zasoba = sklad[kod_soucastky]
        
        if pozadovane_mnozstvi > zasoba:
            print(f"Lze prodat pouze {zasoba} kusů součástky {kod_soucastky}.")
            del sklad[kod_soucastky]
        else:
            print("Poptávku lze uspokojit v plné výši.")
            sklad[kod_soucastky] -= pozadovane_mnozstvi

prodej_soucastky()

pokracovani = input("Přejete si pokračovat v nákupu? (Ano/Ne): ")
if pokracovani == "Ano":
    prodej_soucastky()
else:
    print("Naviděnou příště!")
    