def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

values_list = [False, 20, 'stop']
values_dict = {'a': 'go', 'b': 1.25, 'c': 15}
values_list_2 = [54.32, 'Строка' ]

print_params(*values_list_2, 42)

print_params(b=25)
print_params(c = [1,2,3])
print_params(values_list)
print_params(*values_list)
print_params(values_dict)
print_params(**values_dict)