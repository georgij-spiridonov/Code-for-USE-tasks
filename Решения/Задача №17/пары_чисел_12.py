#чтение файла
file = open('file.txt')
items = []
for item in file.readlines():
    if '\n' in item:
        items.append(int(item[:-1]))
    else:
        items.append(int(item))

#получение минимального
minimum = max(items) + 1
for item in items:
    if str(item)[-1] == '2':
        minimum = min(minimum, item)

#составление и проверка пар
good_pairs = []
for i in range(1, len(items)):
    pair = [items[i-1], items[i]]
    if ((str(pair[0])[-1] == '2' and str(pair[1])[-1] != '2') or (str(pair[1])[-1] == '2' and str(pair[0])[-1] != '2')) and (pair[0] + pair[1]) ** 2 >= minimum ** 2:
        good_pairs.append(pair)

#получение максимального квадрата суммы
max_sum_sq = -1
for pair in good_pairs:
    max_sum_sq = max(max_sum_sq, (pair[0] + pair[1]) ** 2)

#вывод результата
print(f'Количество подходящих пар: {len(good_pairs)}')
print(f'Максимальный квадрат суммы: {max_sum_sq}')