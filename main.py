import random
import pandas as pd

num_wallets = 40  # Кількість гаманців
min_days = '4-7'  # Діапазон активних днів в місяць для кожного гаманця
transactions_range = '1-2'  # Діапазон транзакцій в день у вигляді рядка

min_days_active, max_days_active =  map(int, min_days.split('-'))
min_transactions, max_transactions = map(int, transactions_range.split('-'))

wallets = [f'Wallet_{i+1:02}' for i in range(num_wallets)]
days = range(1, 31)
transactions = []

for wallet in wallets:
    active_days = random.sample(days, random.randint(min_days_active, max_days_active))
    for day in active_days:
        num_transactions = random.randint(min_transactions, max_transactions)
        transactions.append({'Day': day, 'Wallet': wallet, 'Transactions': num_transactions})

df_transactions = pd.DataFrame(transactions)
pivot_table = df_transactions.pivot_table(index='Wallet', columns='Day', values='Transactions', fill_value=0, aggfunc='sum')

pivot_table['Total Transactions'] = pivot_table.sum(axis=1)
pivot_table['Total Active Days'] = (pivot_table.iloc[:, :-1] > 0).sum(axis=1)

totals_row = pd.DataFrame((pivot_table.iloc[:, :-2] > 0).sum().to_frame().T)
totals_row.index = ['Total Wallets']

pivot_table = pd.concat([pivot_table, totals_row])

pivot_table.replace(0, '', inplace=True)

pivot_table.to_csv('pivot_transactions.csv', na_rep='', index=True)

print(pivot_table)
