file = open('file.txt')
items = []
for item in list(file.readlines()):
    items.append(int(str(item)[:-1]))


good_pairs = []
sum_of_pairs = []
for i in range(len(items)):
    pair = [items[i-1], items[i]]
    if sum(pair) % 3 == 0 and sum(pair) % 6 != 0:
        good_pairs.append(pair)
        sum_of_pairs.append(sum(pair))

print('Количество подходящих пар:', len(good_pairs))
print('Максимальная сумма элементов:', max(sum_of_pairs))