d1 = {'Jan': 'January', 'Feb': 'February', 'Mar': 'March'}
print(d1)
print(d1['Feb'])
d2 = {'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Feb': 'Febrero'}
print(d2)

for k in d2.keys():
    print(f'{k}: {d2[k]}')

print('----------')
for k, v in d2.items():
    print(f'{k}: {v}')

print('----------')
for v in d2.values():
    print(v)
