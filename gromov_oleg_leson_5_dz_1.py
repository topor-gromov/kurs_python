def odd_nums(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


max_number = int(input('Введите значение верхней границы генератора(целое положительное число):'))
odd_to_15 = odd_nums(max_number)

if max_number % 2 > 0:
    count_elem = int((max_number // 2) + 1)
else:
    count_elem = int(max_number / 2)

for i in range(count_elem):
    print(next(odd_to_15))

