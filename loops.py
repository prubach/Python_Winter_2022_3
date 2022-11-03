for i in range(5):
    print(f'i={i}')
print('------------')
for i in range(1, 5):
    print(f'i={i}')

print('------------')
for i in reversed(range(1, 5)):
    print(f'i={i}')

print('------------')
for i in reversed(range(-8, 9, 2)):
    print(f'i={i}')

j = 0
while True:
    j += 1 # j = j + 1
    if j == 3:
        continue
    if j == 5:
        break
    print(f'j={j}')

# j = 0
# while j < 7:
#     j += 1 # j = j + 1
#     if j == 3:
#         continue
#     if j == 5:
#         break
#     print(f'j={j}')