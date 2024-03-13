import pandas as pd
df = pd.read_csv('UCI_Credit_Card.txt', delimiter=',')

korelacja = df['AGE'].corr(df['LIMIT_BAL'])
print()
print(f"Korelacja: {korelacja}")

print("\nprzed dodaniem kolumny:\n")
print(df.info())

bill_columns = df.columns[df.columns.str.startswith('BILL_AMT')]

df['SUM_BILL_AMT'] = df[bill_columns].sum(axis=1)

print("\npo dodaniu kolumny:\n")
print(df.info())

print("\npierwsze kilka wierszy")
print(df.head())