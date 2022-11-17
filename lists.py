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
l40 = l4
#TODO extract the word "Python" from l4
#TODO sum up all numbers in l4 (type - use to check the type of variable)

l5 = [x*2 for x in l3]
print(l5)
print('-----------------')

print(f'l4={l4}')
summ=0
for n in l4:
    if isinstance(n, str):  # type(n)==str
        if "Python" in n:
            i = l4.index(n)
            l4[i] = n.replace('Python', '')
    else:
        summ += n

print(f'l4={l4}')
print(f'Sum = {summ}')

print('-----------------')
l4 = [14231, 2523, 252, 'Hello from Python 3', 7578, 967]
print(l4)
l5 = l4[3].split()
print(l5)
l5.remove('Python')
print(l5)
l6 = ' '.join(l5)
l4.remove('Hello from Python 3')
l4.insert(3, l6)
print('Extracting the word Python:',l4)
l4.remove('Hello from 3')
print(l4)
l4.insert(3,3)
print(l4)
list1 = l4
total = sum(list1)
print('Sum of all number in l4:',total)

print('-----------------')

l41 = []
summm = 0
for item in l40:
    if isinstance(item, str):
        if "Python" in item:
            item = item.replace("Python", "")
    if isinstance(item, (int, float, complex)):
        summm += item
    l41.append(item)
print(l41)
print(summm)

print('-----------------')

l4 = [14231, 2523, 252, 'Hello from Python 3', 7578, 967]
#TODO extract the word "Python" from l4
def extract(x):
    return ''.join([i[11:17] for i in x if type(i) == str])
print(extract(l4))
#TODO sum up all numbers in l4 (type - use to check the type of variable)
print(type(l4[0]))
print(type(l4[1]))
print(type(l4[2]))
print(type(l4[3]))
print(type(l4[4]))
print(type(l4[5]))
def sumup(x):
    return sum([i for i in x if isinstance(i, (int, float, complex))])
print(sumup(l4))
