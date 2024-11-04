'''
Zadanie 1. Problem Podziału Paczek (Prograowanie Proceduralne)
Mamy listę paczek o różnych wagach oraz maksymalną wagę, jaką może unieść kurier w jednym kursie.
Twoim zadaniem jest podzielić paczki na jak najmniejszą liczbę kursów, aby każda waga nie przekraczała
maksymalnej dozwolonej wagi. Program powinien korzystać z algorytmu zachłannego do optymalizacji
podziału paczek.

Wymagania:
• Napisz funkcję, która przyjmuje listę wag paczek i maksymalną wagę.
• Użyj pętli for i instrukcji warunkowych if, else do iteracyjnego podziału paczek.
• Program powinien zwracać minimalną liczbę kursów oraz listę paczek w każdym kursie.
'''

# Moje rozwiązanie --- do poprawki

wagi = [10, 15, 7, 20, 5, 8, 10]
max_waga = 25

def zadanie1(wagi, max_waga):
    kursy = [] # zmienna do przechowywania kursów

    wagi.sort(reverse=True)

    kurs = [] # pojedyncze dodawane kursy
    #za_ciezkie = [] # za ciezkie paczki

    obciazenie = max_waga
    for paczka in wagi:
        if paczka > max_waga:
            #za_ciezkie.append(paczka)
            continue
        elif paczka > obciazenie:
            kursy.append(kurs)
            kurs = []
            obciazenie = max_waga - paczka
            kurs.append(paczka)
        else:
            obciazenie -= paczka
            kurs.append(paczka)
    return len(kursy), kursy

print(zadanie1(wagi, max_waga))

# Rozwiązanie z zajęć

def podzielPaczki(wagi, max_waga):
    for waga in wagi:
        if waga > max_waga:
            raise ValueError(f"paczka o wadzie {waga} przekracza dozwolona wage {max_waga} kg")
        wagi_sorted = sorted(wagi, reverse=True)
        kursy = []

        for waga in wagi_sorted:
            dodano = False
            for kurs in kursy:
                if sum(kurs) + waga <= max_waga:
                    kurs.append(waga)
                    dodano = True
                    break
            if not dodano:
                kursy.append([waga])
    return len(kursy), kursy


wagi = [2, 3, 5, 6, 2, 1, 2, 3, 8, 8, 1, 2, 4, 5, 2]

max_waga = 10

#print(podzielPaczki(wagi, max_waga))

liczba_kursow, kursy = podzielPaczki(wagi, max_waga)

for i, kurs in enumerate(kursy, 1):
    print (f"kurs {i}: {kurs} - suma wag: {sum(kurs)}")