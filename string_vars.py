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
