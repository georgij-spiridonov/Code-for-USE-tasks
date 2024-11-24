# Описание задачи:
# Рассматривается множество целых чисел, принадлежащих числовому отрезку [50000; 100000], которые имеют ровно два четных и два нечетных делителя, не считая единицы и самого числа. Найдите количество таких чисел и максимальное из них. В ответе запишите через пробел сначала количество чисел, затем максимальное из них.


count_valid_numbers = 0
largest_valid_number = 0

# Перебор всех чисел в диапазоне от 50000 до 100000 включительно
for number in range(50000, 100001):
    even_divisors_count = 0
    odd_divisors_count = 0
    divisor = 2

    # Поиск делителей числа
    while divisor ** 2 <= number:
        if number % divisor == 0:
            paired_divisor = number // divisor
            for current_divisor in (divisor, paired_divisor):
                if current_divisor % 2 == 0:
                    even_divisors_count += 1
                else:
                    odd_divisors_count += 1
        divisor += 1

    # Проверка условия: количество чётных и нечётных делителей должно быть равно 2
    if even_divisors_count == 2 and odd_divisors_count == 2:
        count_valid_numbers += 1
        largest_valid_number = number

# Вывод результата
print(count_valid_numbers, largest_valid_number)
