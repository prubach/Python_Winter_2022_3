t1 = (353, 366, 37893, 78)
print(t1[1])
#t1[1] = 52
print(t1[1:3])

t2 = (5235, 6747, 4747)
t2_1, t2_2, _ = t2
print(t2_1)
print(t2_2)

print('---------')
print(t1)
l1 = list(t1)
print(l1)
l1.extend([78, 353.76, 366])
#l1.insert(0, [78, 353.76, 366])
print(l1)

s1 = set(l1)
print(s1)
#print(s1[1])
for el in s1:
    print(el)