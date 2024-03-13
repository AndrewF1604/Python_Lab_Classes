import pickle
import os

def zapisz_na_dysku(funkcja):
    def opakowanie(*args, **kwargs):
        nazwa_pliku = f"{funkcja.__name__}_wynik123.txt"

        if os.path.exists(nazwa_pliku):
            with open(nazwa_pliku, 'rb') as plik:
                wczytane_dane = pickle.load(plik)

                if isinstance(wczytane_dane, tuple) and len(wczytane_dane) == 2:
                    (zapisane_argumenty, wynik) = wczytane_dane

                    if zapisane_argumenty == (args, kwargs):
                        print(f"Wynik wczytany z pliku dla {funkcja.__name__}")
                        return wynik

        wynik = funkcja(*args, **kwargs)
        with open(nazwa_pliku, 'wb') as plik:
            pickle.dump(((args, kwargs), wynik), plik)
            print(f"Wynik zapisany do pliku dla {funkcja.__name__}")

        return wynik

    return opakowanie



'''
@zapisz_na_dysku
def fib_rekurencyjnie(n):
    print("liczymy")
    if n <= 1:
        return n
    else:
        return fib_rekurencyjnie(n-1) + fib_rekurencyjnie(n-2)
'''

@zapisz_na_dysku
def fib_rekurencyjnie(n, a=0, b=1):
    print("liczymy")
    if n == 0:
        return a
    else:
        return fib_rekurencyjnie(n - 1, b, a + b)


wynik = fib_rekurencyjnie(17)
print(f"Wynik funkcji Fibonacciego: {wynik}")


