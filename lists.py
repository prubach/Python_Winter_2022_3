l1 = [14231, 2523, 252, 7578, 967]
print(l1)
print(l1[2])
print(l1[1:4])
l1.append(4754)
print(l1)
l1.insert(2, 4235634)
print(l1)
l1.remove(252)
print(l1)
l1.pop(4)
print(l1)

for i in range(len(l1)):
    print(f'el {i}={l1[i]}')

print('-------')

for val in l1:
    print(f'val={val}')

l2 = l1
print(f'l2={l2}')
l3 = l1.copy()
print('-------')
l1.sort()
print(l1)
l1.sort(reverse=True)
l2.sort()
print(f'l1={l1}')
print(f'l2={l2}')
print(f'l3={l3}')

l4 = [14231, 2523, 252, 'Hello from Python 3', 7578, 967]
#TODO extract the word "Python" from l4
#TODO sum up all numbers in l4 (type - use to check the type of variable)

l5 = [x*2 for x in l3]
print(l5)