import json

# Загружаем данные
with open('task1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Посчитать общую сумму расходов
total = sum(item['сумма'] for item in data)
print(f"Общая сумма расходов: {total}")

# Вывести категорию, на которую потрачено больше всего денег
categories = {}
for item in data:
    cat = item['категория']
    categories[cat] = categories.get(cat, 0) + item['сумма']

max_category = max(categories, key=categories.get)
print(f"Больше всего потрачено на: {max_category} ({categories[max_category]} руб.)")
print(f"Расходы по категориям: {categories}")

# самый дорогой день
dates = {}
for item in data:
    date = item['дата']
    dates[date] = dates.get(date, 0) + item['сумма']

max_date = max(dates, key=dates.get)
print(f"Самый дорогой день: {max_date} ({dates[max_date]} руб.)")
print(f"Расходы по дням: {dates}")