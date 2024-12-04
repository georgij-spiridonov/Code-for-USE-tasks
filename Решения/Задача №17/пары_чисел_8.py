#открытие файла и получение списка значений
file = open('file.txt')
items = []
for item in file.readlines():
    items.append(int(item[:-1]))

#получение минимального
minimum = 10 * 10*10
for item in items:
    if item % 19 == 0:
        minimum = min(item, minimum)

#составление и перебор пар
good_pairs = []
for i in range(1, len(items)):
    pair = [items[i-1], items[i]]
    if pair[0] % minimum == 0 or pair[1] % minimum == 0:
        good_pairs.append(pair)

#максимальная сумма
max_sum = 0
for pair in good_pairs:
    max_sum = max(max_sum, sum(pair))

#вывод ответа
print('Количество пар:', len(good_pairs))
print('Максимальная сумма:', max_sum)