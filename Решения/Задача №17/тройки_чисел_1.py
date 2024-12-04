file = open('file.txt')
items = []
for item in list(file.readlines()):
    items.append(int(item[:-1]))

def divider(x, y, z):
    counter = 0
    if x % 7 == 0:
        counter += 1
    if y % 7 == 0:
        counter += 1
    if z % 7 == 0:
        counter += 1
    if counter >= 2:
        return True
    else:
        return False

average = sum(items)/len(items)

good_trios = []
for i in range(2, len(items)):
    nums = [items[i-2], items[i-1], items[i]]
    if (nums[0] < average or nums[1] < average or nums[2] < average) and divider(nums[0], nums[1], nums[2]):
        good_trios.append(nums)
    

max_sum = 0
for pair in good_trios:
    max_sum = max(max_sum, pair[0] + pair[1] + pair[2])

print('Количество подходящих троек:', len(good_trios))
print('Максимальная сумма чисел:', max_sum)