file = open('file.txt')
items = []
for item in list(file.readlines()):
    items.append(int(item[:-1]))

good_pairs = []
for i in range(len(items)):
    nums = [items[i-1], items[i]]
    if nums[0] % 9 == 0 and nums[1] % 9 == 0:
        good_pairs.append(nums)

minimum = 10*100
for pair in good_pairs:
    if sum(pair) < minimum:
        minimum = sum(pair)
print('Количество подходящих пар:', len(good_pairs))
print('Минимальная из сумм чисел подходящих пар:', minimum)


file.close()