
class Pracownik:
    def __init__(self, imie, wynagrodzenie):
        self.imie = imie
        self.wynagrodzenie = wynagrodzenie

    def imie(self, imie) -> str:
        return imie

    def wynagrodzenie_netto(self) ->float:
        brutto = float(self.wynagrodzenie)
        pkt_c = round(brutto * 0.0976, 2) + round(brutto * 0.015, 2) + round(brutto * 0.0245, 2)
        pkt_c = round(pkt_c, 2)
        pkt_d = brutto - pkt_c
        pkt_d = round(pkt_d, 2)
        pkt_e = pkt_d * 0.09
        pkt_e = round(pkt_e, 2)
        pkt_f = pkt_d * 0.0775
        pkt_f = round(pkt_f, 2)
        pkt_h = brutto - pkt_c - 111.25
        pkt_h = round(pkt_h, 0)
        pkt_i0 = pkt_h * 0.18
        pkt_i = round(pkt_i0,2) - 46.33
        pkt_i = round(pkt_i, 2)
        pkt_j = round((pkt_i - pkt_f), 0)
        pkt_j = round(pkt_j, 0)
        wynagrodzenie_netto = brutto - pkt_c - pkt_e - pkt_j
        wynagrodzenie_netto_p = round(wynagrodzenie_netto, 2)
        return wynagrodzenie_netto_p
    def skladki(self) -> float:
        brutto = float(self.wynagrodzenie)
        skladka = round(brutto * 0.0976, 2) + round(brutto * 0.065, 2) + round(brutto * 0.0193, 2) + round(brutto * 0.0245, 2) + round(brutto * 0.0010, 2)
        return round(skladka,2)
    def laczny_koszt(self) -> float:
        brutto = float(self.wynagrodzenie)
        skladka = self.skladki()
        laczny_koszt = round(brutto, 2) + skladka
        return round(laczny_koszt,2)


liczba_pracownikow = input()
suma = 0.0
for i in range(int(liczba_pracownikow)):
    dane_pracownika = input()
    dane_pracownika = dane_pracownika.split(" ")
    imie = dane_pracownika[0]
    wynagrodzenie = int(dane_pracownika[1])
    pracus = Pracownik(imie,wynagrodzenie)
    suma += pracus.laczny_koszt()
    print(imie, '%.2f' %pracus.wynagrodzenie_netto(), '%.2f' %pracus.skladki(), '%.2f' %pracus.laczny_koszt())

print(round(suma,2))



