#получение строки
stroke = '>' + 30 * '1' + 20 * '2' + 10 * '3'

#выполнение замен
while '>1' in stroke or '>2' in stroke or '>3' in stroke:
    if '>1' in stroke:
        stroke = stroke.replace('>1', '2>3', 1)
    if '>2' in stroke:
        stroke = stroke.replace('>2', '33>', 1)
    if '>3' in stroke:
        stroke = stroke.replace('>3', '1>22', 1)

#поиск суммы
items = []
for symbol in stroke:
    if symbol != '>':
        items.append(int(symbol))

print(sum(items))