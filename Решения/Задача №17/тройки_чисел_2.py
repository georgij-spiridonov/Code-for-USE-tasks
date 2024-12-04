file = open('file.txt')
items = []
for item in list(file.readlines()):
    items.append(int(str(item)[:-1]))

good_trios = []
sum_of_trios = []
for i in range(2, len(items)):
    trio = [items[i-2], items[i-1], items[i]]
    if trio[0] < trio[1] and trio[1] < trio[2]:
        good_trios.append(trio)
        sum_of_trios.append(sum(trio))
    

print('Количество подходящих троек:', len(good_trios))
print('Максимальная сумма элементов:', max(sum_of_trios))