for n in range(0, 100000):
    stroke = '>' + 19 * '0' + n * '1' + 36 * '2'
    while '>1' in stroke or '>2' in stroke or '>0' in stroke:
        if '>1' in stroke:
            stroke = stroke.replace('>1', '23>', 1)
        if '>2' in stroke:
            stroke = stroke.replace('>2', '2>', 1)
        if '>0' in stroke:
            stroke = stroke.replace('>0', '3>', 1)
    list_of_nums = []
    for symbol in stroke:
        if symbol != '>':
            list_of_nums.append(int(symbol))
    if sum(list_of_nums) % 27 == 0:
        print(n)
        break