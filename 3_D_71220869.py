a = int(input('Masukkan awal deret: '))
b = int(input('Masukkan akhir deret: '))
d = ['']
while a <= b:
    None if (a % 6) == 0 or (a % 8) == 0 else d.append(str(a))
    a = a + 1
print (('  ').join(d))