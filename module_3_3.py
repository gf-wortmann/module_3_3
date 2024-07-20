# Домашнее задание по уроку "Распаковка позиционных параметров".

def print_params(a=1, b='the string', c=True):
    print(f'a = {a}, b = {b}, c = {c}')


print_params()
print_params(2, 'rake')
print_params(2, 'rake', False)

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [3, [2, 3, 4, ], 'applaud']
values_list_2 = [54.32, 'Строка']
values_dict = {'a': 11, 'b': 'yet another string', 'c': False}

print_params(*values_list)
print_params(*values_list_2, 42)
print_params(**values_dict)
