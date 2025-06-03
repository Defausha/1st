dict_a = {'Alex':12, 'Olga':16}
dict_b = {'Boris':9, 'Kostya':10}
dict_c = {'Ira':11, 'Vova':6}

dict_c.update(dict_a)
dict_c.update(dict_b)
print(dict_c)  # {'Ira': 11, 'Vova': 6, 'Alex': 12, 'Olga': 16, 'Boris': 9, 'Kostya': 10}

dict_c.sorted_keys = sorted(dict_c.keys())
print(dict_c.sorted_keys)  # ['Alex', 'Boris', 'Ira', 'Kostya', 'Olga', 'Vova']