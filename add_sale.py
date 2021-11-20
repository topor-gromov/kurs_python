import sys

if len(sys.argv) > 1:
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        for arg in sys.argv[1:]:  # Если ввели более одного числа в качестве аргумента, вносим их в порядке ввода.
            f.writelines(arg + '\n')
else:
    print('Вы не ввели сумму продажи!')