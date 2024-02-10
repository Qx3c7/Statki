from random import randint


def tworzenie_macierzy(wysokosc, szerokosc): # Tworzenie Tablicy bedącej planszą gry
    tablica = []
    for i in range(wysokosc):
        wyraz = []
        for e in range(szerokosc):
            znak = ' '
            wyraz.append(znak)
        tablica.append(wyraz)
    return tablica


def ustawianie_statkow(tablica, ilosc, wysokosc, szerokosc): # losowanie rozmieszczenia statków
    licznik = 0
    while licznik < ilosc:
        rzad = randint(0, szerokosc - 1)
        szereg = randint(0, wysokosc - 1)
        if tablica[szereg][rzad] == "S":
            continue
        else:
            tablica[szereg][rzad] = 'S'
            licznik += 1


def wyswietl(tablica): # Wyświetlanie planszy gry
    licznik = 0
    print('  X 1   2   3   4   5   6   ')
    print('Y  ------------------------')
    for i in tablica:
        print('{} | {} | {} | {} | {} | {} | {} |'.format(licznik+1, i[0], i[1], i[2], i[3], i[4], i[5]))
        print('   ------------------------')
        licznik += 1


def strzal(macierz, macierz_widzialna, ilosc_strzalow, koordynat_x, koordynat_y): # sprawdzenie trafienia statku
    if macierz[koordynat_x][koordynat_y] == "S":
        macierz[koordynat_x][koordynat_y] = 'X'
        macierz_widzialna[koordynat_x][koordynat_y] = 'X'
        print('Trafiłes statek. Zostało ci tyle strzałów: %d ' % ilosc_strzalow)
        return True
    else:
        macierz_widzialna[koordynat_x][koordynat_y] = '-'
        ilosc_strzalow -= 1
        print('Nie trafiłeś. Zostało ci tyle strzałów: %d' % ilosc_strzalow)
        return False


def menu():
    print('wybierz co zrobić.')
    print('1. rozpoczęcie gry.')
    print('0. Wyjscie z programu')


if __name__ == '__main__':
    wysokoscc = 6       # Podstawowe wartosci programu
    szerokoscc = 6
    strzaly = 5
    ilosc_statkow = 4

    # Tworzenie środowiska gry
    tab = tworzenie_macierzy(wysokoscc, szerokoscc)
    ustawianie_statkow(tab, ilosc_statkow, wysokoscc, szerokoscc)
    widzialna_tab = tworzenie_macierzy(wysokoscc, szerokoscc)
    menu()

    while True:
        wybor = input('Podaj opcje która chcesz wybrać: ')
        try:
            wybor = int(wybor)
        except ValueError:
            continue
        if wybor == 1:
            print()
            wyswietl(widzialna_tab)
            while strzaly > 0: 
                while True:
                    coord_x = input('Podaj koordynat X: ')
                    coord_y = input('Podaj koordynat Y: ')
                    print()
                    try:
                        coord_x = int(coord_x) - 1
                        coord_y = int(coord_y) - 1
                    except ValueError:
                        print('nie podałes cyfr')
                        continue
                    if coord_x < 0 or coord_y < 0:
                        print('Koordynaty sa zza niskie!')
                        continue
                    elif coord_x > wysokoscc or coord_y > szerokoscc:
                        print('Koordynaty sa zza wysokie!')
                        continue
                    break
                wynik = strzal(tab, widzialna_tab, strzaly, coord_y, coord_x)
                if not wynik:
                    strzaly -= 1
                else:
                    ilosc_statkow -= 1
                wyswietl(widzialna_tab)
                if ilosc_statkow == 0 or strzaly == 0:
                    if ilosc_statkow == 0:
                        print('Wygrałes! Gratulacje!')
                    else:
                        print('Porażka!')
                    strzaly = 5
                    print('Czy chcesz wrocić do menu: T-Tak, N-Nie.')

                    wybor2 = input('----> ')
                    if wybor2 == 'N' or wybor2 == 'n':
                        wybor = 0
                        break
                    else:
                        wybor = 'new'
                        break

        if wybor == 0:
            exit()
        elif wybor == 'new':
            strzaly = 5
            ilosc_statkow = 4
            tab = tworzenie_macierzy(wysokoscc, szerokoscc)
            ustawianie_statkow(tab, ilosc_statkow, wysokoscc, szerokoscc)
            widzialna_tab = tworzenie_macierzy(wysokoscc, szerokoscc)
        menu()
    print('Do widzenia!')
