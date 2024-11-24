list_x = []
for x in range(0, 100):
    text = '>' + 37 * '1' + x * '2' + 37 * '3'
    while '>1' in text or '>2' in text or '>3' in text:
        text = text.replace('>1', '2>', 1)
        text = text.replace('>2', '3>', 1)
        text = text.replace('>3', '1>', 1)

    summ = text.count('1') + text.count('2') * 2  + text.count('3') * 3
    if summ % 17 == 0:
        list_x.append(x)

print(min(list_x))