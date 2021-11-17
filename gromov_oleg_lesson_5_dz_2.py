
max_number = int(input('Введите значение верхней границы генератора(целое положительное число):'))

odd_to_15 = (num for num in range(1, max_number+1, 2))

if max_number % 2 > 0:
    count_elem = int((max_number // 2) + 1)
else:
    count_elem = int(max_number / 2)

for i in range(count_elem):
    print(next(odd_to_15))