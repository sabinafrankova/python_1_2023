def overeni_tel_cisla(cislo):
    return len(cislo) == 9 or (len(cislo) == 13 and cislo[0:4] == "+420")

def spocti_cenu_zpravy(zprava):
    if len(zprava) % 180 == 0:
        cena = (len(zprava) // 180) * 3
    else:
        cena = ((len(zprava) // 180) + 1) * 3
    return cena

def main():
    cislo = input("Zadejte telefonní číslo: ")
    if not overeni_tel_cisla(cislo):  # Opraveno jméno funkce
        print("Neplatné telefonní číslo!")
        return

    zprava = input("Zadejte zprávu k odeslání: ")
    cena = spocti_cenu_zpravy(zprava)

    print(f"Cena zprávy je {cena} Kč.")

if __name__ == "__main__":
    main()