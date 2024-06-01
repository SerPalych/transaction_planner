# Генератор планування транзакцій

Цей проект генерує зведену таблицю транзакцій для заданої кількості гаманців, кожен з яких має випадкову кількість активних днів у місяці та випадкову кількість транзакцій у день. Таблиця показує кількість транзакцій для кожного дня місяця для кожного гаманця, а також підсумкову інформацію про загальну кількість транзакцій та активних днів для кожного гаманця.

Таблиця зберігається у файлі `pivot_transactions.csv`

![Screenshot](https://github.com/SerPalych/transaction_planner/assets/95444023/9ddde9dd-911a-4518-8eb7-0735772c043f)


## Встановлення

1. Клонувати репозиторій:
    ```bash
    git clone https://github.com/SerPalych/transaction_planner.git
    cd transaction_planner
    ```

2. Встановити необхідні пакети:
    ```bash
    pip install pandas
    ```

## Використання

Скрипт можна запустити безпосередньо з командного рядка:
```bash
python main.py
```

## Конфігурація

Скрипт має наступні параметри, які можна змінити у коді:

- `num_wallets`: кількість гаманців.
- `min_days`: діапазон активних днів в місяць для кожного гаманця (у форматі 'мінімум-максимум').
- `transactions_range`: діапазон транзакцій в день для кожного гаманця (у форматі 'мінімум-максимум').
