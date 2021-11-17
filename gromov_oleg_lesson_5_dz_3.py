tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена','Руслан', 'Светлана', 'Роман']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
import itertools

gen_result = (num for num in itertools.zip_longest(tutors, klasses, fillvalue='None'))

print(type(gen_result))

for i in range(len(tutors)):
    print(next(gen_result))
