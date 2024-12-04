#получение данных из файла
file = open('file.txt')
items = []
for item in file.readlines():
    items.append(int(item[:-1]))

#нахождение минимального элемента
minimum = max(items) + 1
for item in items:
    if str(item)[-1] == '4':
        minimum = min(minimum, item)

#составление и проверка пар
good_pairs = []
for i in range(1, len(items)):
    pair = [items[i-1], items[i]]
    # print(pair)
    # break
    if (str(pair[0])[-1] == '4' and str(pair[1])[-1] != '4' and sum(pair)**2 >= abs(minimum)) or (str(pair[0])[-1] != '4' and str(pair[1])[-1] == '4' and sum(pair)**2 >= abs(minimum)):
        good_pairs.append(pair)

#поиск максимального квадрата суммы
max_sum_sq = -1
for pair in good_pairs:
    max_sum_sq = max(max_sum_sq, sum(pair)**2)

#вывод результатов
print('Количество подходящих пар:', len(good_pairs))
print('Максимальный квадрат суммы:', max_sum_sq)