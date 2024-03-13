import pandas as pd
import matplotlib.pyplot as plt

# Wczytaj dane z pliku TXT
df = pd.read_csv('UCI_Credit_Card.txt', delimiter=',')

# Utwórz subploty
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Histogram limitu kredytu
axs[0, 0].hist(df['LIMIT_BAL'], bins=20, color='blue', edgecolor='black')
axs[0, 0].set_title('Histogram Limitu Kredytu')
axs[0, 0].set_xlabel('Limit Kredytu')
axs[0, 0].set_ylabel('Liczba klientów')

# Histogram wieku
axs[0, 1].hist(df['AGE'], bins=20, color='green', edgecolor='black')
axs[0, 1].set_title('Histogram Wieku')
axs[0, 1].set_xlabel('Wiek')
axs[0, 1].set_ylabel('Liczba klientów')

# Zależność limitu kredytu od wieku
axs[1, 0].scatter(df['AGE'], df['LIMIT_BAL'], alpha=0.5, color='red')
axs[1, 0].set_title('Zależność Limitu Kredytu od Wieku')
axs[1, 0].set_xlabel('Wiek')
axs[1, 0].set_ylabel('Limit Kredytu')

# Usuń puste subploty
fig.delaxes(axs[1, 1])

# Dostosuj układ
plt.tight_layout()

# Wyświetl wykres
plt.show()