from itertools import zip_longest
from itertools import islice
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Андрей', 'Павел']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

my_cor = ((tut, kla) for tut, kla in zip_longest(tutors, klasses))

print(type(my_cor))
print(*my_cor)
print(*islice(my_cor, 100))