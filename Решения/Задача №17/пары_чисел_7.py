file = open('file.txt')
items = []
for item in list(file.readlines()):
    items.append(int(str(item)[:-1]))
average = sum(items)/len(items)

def get_dif(number_1, number_2):
    if abs(number_1 - number_2) <= 20:
        return True
    else:
        return False

good_pairs = []
sum_of_pairs = []
for i in range(len(items)):
    pair = [items[i-1], items[i]]
    if get_dif(pair[0], pair[1]) and sum(pair) > average:
        good_pairs.append(pair)
        sum_of_pairs.append(sum(pair))

print('Количество подходящих пар:', len(good_pairs))
print('Максимальная сумма чисел:', max(sum_of_pairs))