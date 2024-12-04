#получение данных
file = open('file.txt')
items = []
for item in file.readlines():
    items.append(int(item[:-1]))

#определение количества чисел, кратных 32
count = 0
for item in items:
    if item % 32 == 0:
        count += 1

#создание и проверка пар
good_pairs = []
for i in range(1, len(items)):
    pair = [items[i-1], items[i]]
    if (pair[0] < 0 or pair[1] < 0) and sum(pair) < count:
        good_pairs.append(pair)

#поиск максимального квадрата суммы
max_sum = min(items)
for pair in good_pairs:
    max_sum = max(max_sum, sum(pair))

#вывод результатов
print(f'Количество подходящих пар: {len(good_pairs)}')
print(f'Максимальная сумма: {max_sum}')