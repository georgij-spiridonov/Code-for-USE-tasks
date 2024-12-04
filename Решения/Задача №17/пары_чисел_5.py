file = open('file.txt')
items = []
for item in list(file.readlines()):
    items.append(int(item[:-1]))

good_pairs = []
for i in range(len(items)):
    nums = [items[i-1], items[i]]
    if sum(nums)**2 % 7 == 0:
        good_pairs.append(nums)

max_sum_sq = 0
for pair in good_pairs:
    max_sum_sq = max(max_sum_sq, pair[0]**2 + pair[1]**2)

print('Количество подходящих пар:', len(good_pairs))
print('Максимальный квадрат суммы чисел:', max_sum_sq)