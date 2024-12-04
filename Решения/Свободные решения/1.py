def dividers(number, a, x, y, z, w):
    if number % a == 0:
        if number % x != 0:
            if number % y != 0:
                if number % z != 0:
                    if number % w != 0:
                        return True
good_numbers = []
for number in range(924, 9432 + 1):
    if dividers(number, 7, 11, 13, 15, 24):
        good_numbers.append(number)

print(len(good_numbers), max(good_numbers))


# Рассматривается множество целых чисел, принадлежащих отрезку [924; 9432], которые делятся на 7 и не делятся на 11, 13, 15 и 24. Найдите количество таких чисел и максимальное из них. В ответе запишите два числа без пробела подряд: сначала количество, затем максимальное число.