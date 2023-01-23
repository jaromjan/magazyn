# pogram ksiegowy - magazyn
historia_dl = 0
historia = {}
magazyn = {}
magazyn_add = []
magazyn_mv = []
konto = float(0)
dostepne_operacje = ['saldo', 'sprzedaz', 'zakup', 'konto', 'lista', 'magazyn', 'przeglad', 'koniec']
# pobieramy i weryfikujemy dostepnosc operacji
while True:
    while True:
        print(f"Dostepne operacje: {dostepne_operacje}")
        operacja = input("Podaj operacje: ")
        if operacja in dostepne_operacje:
            break
        else:
            print("Operacja z poza listy dostępnych operacji")
# wykonujemy zadane operacje
    if operacja == "saldo":
        saldo_add = input("Podaj kwote do dodania(odjęcia) do konta <int>/<float>: ")
        if saldo_add != '':
            if konto + float(saldo_add) < 0:
                print("Operacja niemozliwa do wykonania")
            else:
                konto += float(saldo_add)
                historia_dl = len(historia)
                historia[(historia_dl + 1)] = ['saldo', float(saldo_add)]
        else:
            print("Podano pustą wartosc - operacja niemozliwa do wykonania")
    elif operacja == "sprzedaz":
        nazwa = input("Podaj nazwe produktu: ")
        cena = input("Podaj cene produktu<int><float>: ")
        ilosc = input("Podaj ilosc produktow<int>: ")
        # weryfikujemy poprawnosc zlecenia
        if nazwa == '' or cena == '' or ilosc == '':
            print("Operacja niemozliwa - podano pusta wartosc")
        else:
            # sprawdzamy poprawnosc ceny i ilosci
            noint = 0
            for y in cena:
                if y not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'):
                    noint = 1
            for z in ilosc:
                if z not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                    noint = 1
            if noint == 1 or cena == '0' or ilosc == '0':
                print("Przynajmniej  jedna podana wartosc jest niepoprawna")
            else:
                ilosc = int(ilosc)
                # jako identyfikatora uzyjemy sumy nazwy i ceny - bo mozemy miec te same produkty o roznych cenach
                magazyn_mv = nazwa + cena, nazwa, float(cena), ilosc
                # sprawdzamy czy mamy taki produkt
                if magazyn_mv[0] not in magazyn:
                    print("Produktu o takiej nazwie i cenie niema w magazynie")
                else:
                    # sprawdzamy czy mamy wystarczajaca ilosc sztuk
                    if ilosc > magazyn[magazyn_mv[0]][2]:
                        print(f"Dostepna ilosc produktu jest mniejsza i wynosi: {magazyn[magazyn_mv[0]][2]}")
                    else:
                        # jesli zlecenie zabiera wszystkie sztuki produktu usuwamy produkt z magazynu
                        if ilosc == magazyn[magazyn_mv[0]][2]:
                            del magazyn[magazyn_mv[0]]
                            konto += magazyn_mv[2] * magazyn_mv[3]
                            print(f"Sprzedano caly zapas produktu o nazwie: {magazyn_mv[1]} i cenie: {magazyn_mv[2]}")
                            historia_dl = len(historia)
                            historia[(historia_dl + 1)] = ['sprzedaz', [nazwa, float(cena), ilosc]]
                        # jesli taki produkt istnieje modyfikujemy tylko ilosc sztuk
                        else:
                            x = magazyn[magazyn_mv[0]][1]
                            y = magazyn[magazyn_mv[0]][2] - ilosc
                            magazyn[magazyn_mv[0]] = [nazwa, x, y]
                            konto += magazyn_mv[2] * magazyn_mv[3]
                            print(f"Zmodyfikowano ilosc produktu o nazwie: {magazyn_mv[1]} i cenie: {magazyn_mv[2]} "
                                  f"obecny stan to {magazyn[magazyn_mv[0]][2]}")
                            historia_dl = len(historia)
                            historia[(historia_dl + 1)] = ['sprzedaz', [nazwa, float(cena), ilosc]]
    # zakup - wprowadzamy zakupiony produkt do magazynu
    elif operacja == "zakup":
        nazwa = input("Podaj nazwe produktu: ")
        cena = input("Podaj cene produktu<int><float>: ")
        ilosc = input("Podaj ilosc produktow<int>: ")
        if nazwa == '' or cena == '' or ilosc == '':
            print("Operacja niemozliwa - podano pusta wartosc")
        else:
            # sprawdzamy poprawnosc ceny i ilosci
            noint = 0
            for y in cena:
                if y not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'):
                    noint = 1
            for z in ilosc:
                if z not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                    noint = 1
            if noint == 1 or cena == '0' or ilosc == '0':
                print("Przynajmniej  jedna podana wartosc jest niepoprawna")
            else:
                ilosc = int(ilosc)
                # jako identyfikatora uzyjemy sumy nazwy i ceny - bo mozemy miec te same produkty o roznych cenach
                magazyn_add = nazwa + cena, nazwa, float(cena), ilosc
                # Najpierw sprawdzamy czy mamy wystarczajace srodki na koncie
                if konto < (float(magazyn_add[2]) * int(magazyn_add[3])):
                    print("Operacja niemozliwa - brak wystarczajacych srodkow na koncie")
                else:
                    if magazyn_add[0] not in magazyn:
                        # jesli takiego produktu niema w magazynie dopisujemy do magazynu
                        magazyn[magazyn_add[0]] = [magazyn_add[1], magazyn_add[2], magazyn_add[3]]
                        konto -= magazyn_add[2] * magazyn_add[3]
                        print("Dodano produkt do magazynu")
                        historia_dl = len(historia)
                        historia[(historia_dl + 1)] = ['zakup', [nazwa, float(cena), ilosc]]
                    else:
                        # jesli taki produkt istnieje dodajemy tylko ilosc sztuk
                        x = magazyn[magazyn_add[0]][1]
                        y = magazyn[magazyn_add[0]][2] + ilosc
                        magazyn[magazyn_add[0]] = [nazwa, x, y]
                        konto -= magazyn_add[2] * magazyn_add[3]
                        print("Zmodyfikowano liczbe produktow w magazynie")
                        historia_dl = len(historia)
                        historia[(historia_dl + 1)] = ['zakup', [nazwa, float(cena), ilosc]]
    # konto - wyswietlamy stan konta
    elif operacja == "konto":
        print(f"Stan konta wynosi: {konto}")
    # lista - wyswietlamy stan magazynu
    elif operacja == "lista":
        print("Stan magazynu: ")
        komunikat = "Magazyn jest pusty"
        for i in magazyn:
            print(f"Nazwa: {magazyn[i][0]}, cena: {magazyn[i][1]}, ilosc: {magazyn[i][2]}")
            komunikat = ''
        if komunikat != '':
            print(komunikat)
    # magazyn - wyswietalmy stan magazynu dla danego produktu
    elif operacja == "magazyn":
        produkt = input("Podaj nazwe produktu: ")
        kontrolna = 0
        if produkt == '':
            print("Podano pusta nazwa - operacja niemozliwa do wykonania")
        else:
            print("Stan magazynu dla podanego produktu: ")
            info = 'Magazyn jest pusty'
            kontrolna = 1
            for element in magazyn:
                if produkt == magazyn[element][0]:
                    print(f"Nazwa: {magazyn[element][0]}, cena: {magazyn[element][1]}, ilosc: {magazyn[element][2]}")
                    kontrolna = 0
                elif produkt != magazyn[element][0]:
                    info = "Brak w magazynie"
                    kontrolna = 1
            if kontrolna == 1:
                print(info)
    elif operacja == "przeglad":
        if len(historia) < 1:
            print("Brak wpisow")
        else:
            od = input("Podaj numer wpisu od ktorego chcesz rozpoczac<int>: ")
            do = input("Podaj numer wpisu do ktorego chcesz kontynuowac<int>: ")
            if od == '' and do == '':
                print("Podano puste wartosci - wyswietlam cala historia")
                for i in historia:
                    print(i, ": ", historia[i])
            elif od == '' and do != '':
                # sprawdzamy wprowadzona wartosc czy jest int+
                noint = 0
                for y in do:
                    if y not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                        noint = 1
                if noint == 1 or do == '0':
                    print("Podana wartosc jest niepoprawna")
                    print(f"Dopuszczalne wartosci powinny zawierac sie pomiedzy 1 i {len(historia)}")
                else:
                    print("Wyswietlam historie od poczatku do podanej wartosci")
                    for i in historia:
                        if i <= int(do):
                            print(i, ": ", historia[i])
            elif od != '' and do == '':
                noint = 0
                for y in od:
                    if y not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                        noint = 1
                if noint == 1 or od == '0':
                    print("Podana wartosc jest niepoprawna")
                    print(f"Dopuszczalne wartosci powinny zawierac sie pomiedzy 1 i {len(historia)}")
                else:
                    print("Wyswietlam historie od podanej wartosci do konca")
                    for i in historia:
                        if i >= int(od):
                            print(i, ": ", historia[i])
            elif od != '' and do != '':
                noint = 0
                for y in od:
                    if y not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                        noint = 1
                for z in do:
                    if z not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                        noint = 1
                if noint == 1:
                    print("Przynajmniej  jedna podana wartosc jest niepoprawna")
                elif int(od) == 0 or int(do) == 0:
                    print("Podano niedopuszczalna zerowa wartosc")
                    print(f"Dopuszczalne wartosci powinny zawierac sie pomiedzy 1 i {len(historia)}")
                elif int(od) > int(do):
                    print("Wartosc poczatkowa wieksza od koncowej")
                    print(f"Dopuszczalne wartosci powinny zawierac sie pomiedzy 1 i {len(historia)}")
                else:
                    print("Wyswietlam historie dla podanego zakresu wartosci")
                    for i in historia:
                        if int(od) <= i <= int(do):
                            print(i, ": ", historia[i])
    # koniec - konczymy program
    elif operacja == "koniec":
        print("Koniec programu")
        break
