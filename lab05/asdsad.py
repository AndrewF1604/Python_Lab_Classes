import pandas as pd

# Wczytaj dane z pliku TXT
df = pd.read_csv('UCI_Credit_Card.txt', delimiter=',')

# Dodaj kolumnę będącą sumą wszystkich transakcji
df['SUM_BILL_AMT'] = df.filter(like='BILL_AMT').sum(axis=1)

# Wybierz interesujące nas kolumny
selected_columns = ['LIMIT_BAL', 'AGE', 'EDUCATION', 'SUM_BILL_AMT']

# Znajdź 10 najstarszych klientów
top_10_oldest = df.nlargest(10, 'AGE')[selected_columns]

# Wyświetl tabelę
print(top_10_oldest)