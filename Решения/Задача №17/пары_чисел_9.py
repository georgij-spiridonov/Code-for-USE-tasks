#открытие файла и получение списка значений
file = open('file.txt')
items = []
for item in file.readlines():
    items.append(int(item[:-1]))

#получение минимального
minimum = 10 * 10*10
for item in items:
    if str(item)[-1] == '2':
        minimum = min(item, minimum)

#составление и перебор пар
good_pairs = []
for i in range(1, len(items)):
    pair = [items[i-1], items[i]]
    if (str(pair[0])[-1] == '2' and str(pair[1])[-1] != '2' and sum(pair)**2 >= minimum ** 2) or (str(pair[0])[-1] != '2' and str(pair[1])[-1] == '2' and sum(pair)**2 >= minimum ** 2):
        good_pairs.append(pair)

#максимальный квадрат суммы
max_sum_sq = 0
for pair in good_pairs:
    max_sum_sq = max(max_sum_sq, sum(pair)**2)

#вывод ответа
print('Количество пар:', len(good_pairs))
print('Максимальный квадрат суммы:', max_sum_sq)