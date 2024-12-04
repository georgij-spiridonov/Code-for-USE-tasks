#получение данных из файла
file = open('file.txt')
items = []
for item in file.readlines():
    items.append(int(item[:-1]))

#проверка нечётности
def odd(number):
    if number % 2 != 0:
        return True
    else:
        return False

#проверка четвёрок
good_quads = []
for i in range(3, len(items)):
    quad = [items[i-3], items[i-2], items[i-1], items[i]]
    if odd(quad[0]) and odd(quad[1]) and odd(quad[2]) and odd(quad[3]) and '888' in str(sum(quad)):
        good_quads.append(quad)

#вывод ответа
print(len(good_quads))