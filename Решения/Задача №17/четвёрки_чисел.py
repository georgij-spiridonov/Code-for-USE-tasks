file = open('file.txt')
items = []
for item in list(file.readlines()):
    items.append(int(str(item)[:-1]))
average = sum(items)/len(items)

maximum = 0
for i in range(3, len(items)):
    quad = [items[i-3], items[i-2], items[i-1], items[i]]
    maximum = max(sum(quad), maximum)


good_quads = []
sum_of_quads = []
for i in range(3, len(items)):
    quad = [items[i-3], items[i-2], items[i-1], items[i]]
    if sum(quad) == maximum:
        good_quads.append(quad)


print('Максимальная сумма чисел:', maximum)
print('Количество подходящих четвёрок:', len(good_quads))
