import random

def totolotek():
    print("Podaj 6 liczb: ")
    
    wynik = []
    for _ in range(6):
        wynik.append(random.randint(1,20))
    print(wynik)
    liczby = []
    while len(liczby) < 6:
        wpis = input()
        if not wpis.isdigit():
            print("Wprowadziłeś błedną wartość, lub wartość już istnieje")
            continue
        wpis = int(wpis)
        if 0 < wpis <= 20 and wpis not in liczby:
                liczby.append(wpis) 
        else:
            print("Wprowadziłeś błedną wartość, lub wartość już istnieje")
    print(liczby)
    porownanie = [element for element in liczby if element in wynik]
    print(porownanie)
    
totolotek()