def wywiadkom(arg):
    for a in arg:
        print(a)
def poswywiad(lista):
    for i in lista:
        pytanie = input(i)
        i.append("====>")
        i.append(pytanie)


Rodzina = [["wiek i stan zdrowia rodziców?"], ["Wiek, stan zdrowia i płeć rodzeństwa?"],["Stan zdrowia ewentulanych domowników?"],["wysępowanie w rodzinie chorob dziedzicznych?"],["kontakt dziecka z chorobami zakaźnynmi w ostatnich 3 tygodniach"],["kontakt dziecka ze zwierzętami w domui innych środowiskach?"]]
Ciąża = [["która ciąża?"],["przebieg ciąży?"],["choroby w trakcie?"],["leki w trakcie ?"],["praca w trakcie ciązy,papierosy,kontakt ze zwierzętami"],["przebieg poprzednich ciąż"]]
Poród = [["gdzie odbył się porod?"], ["czy porod wystąpił o planowanym czasie"],["PNS czy CC i jeżeli cc to dlaczego?"],["skala Apgar?"]]
Dotychczasowy_rozwoj_dziecka = [["Psychiczny: uśmiech = 3 miesiąc, gaworzenie = 4 msc, pojedyncze słowa = 9 msc, proste zdania = 20msc"], ["rozwój motoryczny: podnosenie głowy = 3 msc, siadanie = 6/7 msc, wstawanie = 9 msc, chód = 12 msc"], ["rozwój motoryczny: pierwszze zęby 6msc,przybieranie na wadze : przez pierwsze 5 msc 700g na miesiac pózniej 500g do 12msc"]]
Żywenie = [["do którego miesiąca było żywione naturlenie"],["jak długo było karmione w sposób mieszany"],["od którego miesiąca sztucznie?"],["kiedy właczone zostały produkty uzupelniajce?"],["Jeżeli dziecko jest na diecie eliminacyjnej, jakie były przyczyny jej właczenia i okres stosowania"],[" ile razy w ciągu dnia jest ono karmione, jakie produkty i w jakiej objętości otrzymuje na poszczególne posiłki."],[" pory spożywania przez nie posiłków, pytając także o produkty spożywcze, których dzieci nie jedzą?"],[" suplementację witaminy D"]]
Szczepienia_ochronne = [["wirusowemu zapaleniu wątroby typu B;"
                         "gruźlicy;"
                         "błonicy;"
                         "tężcowi;"
                         "krztuścowi;"
                         "poliomyelitis;"
                         "odrze;"
                         "nagminnemu zapaleniu przyusznic (śwince);"
                         "różyczce;"
                         "Haemophilus influenzae - w rodzinach wielodzietnych i u dzieci z placówek opiekuńczych;"
                         "ospie wietrznej - jedynie w wybranych ze względów zdrowotnych i epidemiolo- gicznych grupach dzieci do 12. roku życia;"
                         "zakażeniom pneumokokami - jedynie w wybranych ze względów zdrowotnych grupach dzieci od 2. miesiąca życia do 5. roku życia."
                         ]]
Warunki_bytowe = [["zajmowanego przez rodzinę mieszkania"],['liczby osób w nim mieszkających'],["określenia, czy warunki materialne są dobre, wystarczające/mierne czy złe - pyta- nie to określa możliwości rodziców co do zakupu leków wymagających podawania po zakończeniu hospitalizacji"]]
Choroby_przebyte = [["Przebyte choroby"],["przebieg chroób"],["leki"],["choroby zakaźne"]]

Choroba_obecna = [["od kiedy choruje?"],["Jaki był początek choroby - ostry czy objawy nasilały sie stopniowo"],["jakie były początkowe objawy choroby?"],["Jeżeli dziecko było już badane przez lekarza w czasie trwającej choroby, dowiadu- jemy sie, co lekarz rozpoznał, jakie zlecił leczenie, jak matka podawała leki, jaki był efekt leczenia."],["Jaki był dalszy przebieg choroby"],["Czy podobne objawy obserwowano kiedykolwiek w przeszłości?"],["Czy w chwili przeprowadzanego przez nas badania dziecko jest pod wpływem jakiegoś leku"],["charakteru objawów (przewlekły, nawrotowy, napadowy)"],["czasu wystepowania (pora roku, określone miesiące, pora dnia lub nocy);"],["lokalizacji (np. ból brzucha lub głowy może być uogólniony lub może obejmować określoną ich cześć);"],["czasu trwania;"],["sposobu ustepowania (nagle, stopniowo, samoistnie, pod wpływem podanego leku);"],["zachowania sie dziecka w czasie wystepowania objawów chorobowych (bez zmiany zachowania, przyjmowanie pozycji leżącej lub siedzącej, płacz, niepokój, apatia);"],["domniemanego związku przyczynowego z wysiłkiem fizycznym, ze spożyciem określonego pokarmu, zdenerwowaniem"]]


while True:
    print("1 => zbierz nowy wywiad")
    print("2 => zakończ program")
    b = input("wybierz akcje:")
    if b == "1":
        a = input("Imię, nazwisko i wiek")
        poswywiad(Rodzina)
        poswywiad(Ciąża)
        poswywiad(Poród)
        poswywiad(Dotychczasowy_rozwoj_dziecka)
        poswywiad(Żywenie)
        poswywiad(Szczepienia_ochronne)
        poswywiad(Warunki_bytowe)
        poswywiad(Choroby_przebyte)
        poswywiad(Choroba_obecna)


        print(a,"Podsumowanie")
        wywiadkom(Rodzina)
        wywiadkom(Ciąża)
        wywiadkom(Poród)
        wywiadkom(Dotychczasowy_rozwoj_dziecka)
        wywiadkom(Żywenie)
        wywiadkom(Szczepienia_ochronne)
        wywiadkom(Warunki_bytowe)
        wywiadkom(Choroby_przebyte)
        wywiadkom(Choroba_obecna)
    elif b == "2":
        break
    else:
        print("zły wybór")





#Ciąża,Poród,Dotychczasowy_rozwoj_dziecka,Żywenie,Szczepienia_ochronne,Warunki_bytowe,Choroby_przebyte,Choroba_obecna
