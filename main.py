

class Pracownik:
    def __init__(self, imie, wynagrodzenie_netto, skladki, laczny_koszt):
        self.imie = imie
        self.wynagrodzenie_netto = wynagrodzenie_netto
        self.skladki = skladki
        self.laczny_koszt = laczny_koszt

liczba_pracownikow = (input())

for i in range(int(liczba_pracownikow)):
    dane_pracownika = input()
    dane_pracownika = dane_pracownika.split(" ")
    imie_p = str(dane_pracownika[0])
    wynagrodenie = int(dane_pracownika[1])
    brutto = float(wynagrodenie)
    pkt_c = round(brutto*0.0976,2)+round(brutto*0.015,2)+round(brutto*0.0245,2)
    pkt_c = round(pkt_c,2)
    pkt_d = brutto-pkt_c
    pkt_d = round(pkt_d, 2)
    pkt_e = pkt_d*0.09
    pkt_e = round(pkt_e, 2)
    pkt_f = pkt_d*0.0775
    pkt_f = round(pkt_f, 2)
    pkt_h = brutto-pkt_c-111.25
    pkt_h = round(pkt_h, 0)
    pkt_i0 = pkt_h * 0.18
    pkt_i = pkt_i0 - 46.33
    pkt_i = round(pkt_i, 2)
    pkt_j = round((pkt_i-pkt_f),0)
    wynagrodzenie_netto = brutto - pkt_c - pkt_e - pkt_j
    wynagrodzenie_netto_p = round(wynagrodzenie_netto,2)
    skladka = round(brutto*0.0976,2) + round(brutto*0.065,2) + round(brutto*0.0193,2) + round(brutto*0.0245,2) + round(brutto*0.0010,2)
    skladki_p = round(skladka,2)
    laczny_koszt_p = round(brutto, 2)+skladki_p

praco = Pracownik(imie_p, wynagrodzenie_netto_p, skladki_p, laczny_koszt_p)

print(praco.imie, praco.wynagrodzenie_netto, praco.skladki, praco.laczny_koszt)


