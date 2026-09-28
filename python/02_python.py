def analizuj_tekst(tekst: str) -> dict[str, int]:
    """
    Analizuje podany tekst i zwraca słownik ze statystykami.
    Dzięki adnotacjom typów od razu widać, że zwracamy słownik (dict),
    gdzie kluczem jest tekst (str), a wartością liczba (int).
    """
    wynik: dict[str, int] = {
        "dlugosc": len(tekst),
        "ilosc_slow": len(tekst.split())
    }
    return wynik

def main() -> None:
    print("Nowoczesny Python")
    imie: str = input("Podaj swoje imie lub dowolny tekst: ")

    #Funkcja zwroci slownik, z ktorego latwo wyciagniemy dane
    statystyki: dict[str, int] = analizuj_tekst(imie)

    #f-stringi to najnowoczesniejszy sposob formatowania zmiennych w tekscie
    print(f"Witaj {imie}! Twój tekst ma {statystyki['dlugosc']} znaków ")
    print(f"i składa się z {statystyki['ilosc_slow']} słów.")

    #Kod jest wywołany bezpośrednio, a nie imporotwany z zewnatrz

if __name__ == "__main__":
    main()