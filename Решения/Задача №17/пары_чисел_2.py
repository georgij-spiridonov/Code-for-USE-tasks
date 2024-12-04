file = open('file.txt')
items = []
for item in list(file.readlines()):
    items.append(int(item[:-1]))

good_pairs = []
for i in range(len(items)):
    nums = [items[i-1], items[i]]
    if str(nums[0])[-1] in '26' and str(nums[1])[-1] in '26':
        good_pairs.append(nums)
        print(nums)

maximum = -10**100
for pair in good_pairs:
    if sum(pair) % 8 == 0 and sum(pair) > maximum:
        maximum = sum(pair)


print('Количество подходящих пар:', len(good_pairs))
print('Максимальная из подходящих сумм чисел:', maximum)


file.close()