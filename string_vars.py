s1 = 'abcdefghfgh'
print(s1[2])
print(s1[2:6])
print(s1[2:])
print(s1[:2])
print(s1[-2:])
s2 = s1[:2] + s1[-2:]
print(s2)

print(s1.find('fg'))
s3a = '245634636;23623636;2456326;236236'
s3b = "245634636;23623636;2456326;236236"
s4 = "I can't"
s5 = 'He said "my name is...."'
s6 = 'He said "I can\'t"'

print(s3a.split(';'))
print(s3a.split(';')[1])

s5 = 'He said "my name is...."'
s6 = 'He said "I can\'t"'
s6 = "He said \"I can't\""
s6 = "He \\nsaid \"I \tcan't\""
print(s5)
print(s6)

print(ord('a'))
print(ord('Ł'))
print(ord('ś'))

print(chr(65), end='')
print(chr(32), end='')
print(chr(66), end='')