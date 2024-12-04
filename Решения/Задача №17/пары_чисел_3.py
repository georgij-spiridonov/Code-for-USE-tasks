file = open('file.txt')
items = []
for item in list(file.readlines()):
    items.append(int(item[:-1]))

def get_last(number):
    return int(str(number)[-1])

maximum = -20000
for item in items:
    if get_last(item) == 3:
        maximum = max(item, maximum)

good_pairs = []
for i in range(len(items)):
    nums = [items[i-1], items[i]]
    if (get_last(nums[0]) == 3 and get_last(nums[1]) != 3) or (get_last(nums[1]) == 3 and get_last(nums[0]) != 3):
        if (nums[0]**2 + nums[1]**2) >= maximum**2:
            good_pairs.append(nums)

max_sq_sum = 0
for pair in good_pairs:
    max_sq_sum = max(max_sq_sum, pair[0]**2 + pair[1]**2)

print('Количество подходящих пар:', len(good_pairs))
print('Максимальная сумма квадратов чисел:', max_sq_sum)