a = input('Masukkan Nama Lengkap Anda : ')
b = input('Masukkan Prodi Anda : ')
c = input('Masukkan Nilai (dalam huruf) yang Anda Dapat: ').upper()

try :
    if c == 'A':
        print('Nilai anda adalah 4.0, tbl tbl serem bgt lohh')
    elif c == 'A-':
        print('Nilai anda adalah 3.75, kamu keren!')
    elif c == 'B+':
        print('Nilai anda adalah 3.25, kamu keren!')
    elif c == 'B':
        print('Nilai anda adalah 3.0, kamu keren!')
    elif c == 'B-':
        print('Nilai anda adalah 2.75, Kurang semangat belajar nihh')
    elif c == 'C+':
        print('Nilai anda adalah 2.25, kamu keren!')
    elif c == 'C':
        print('Nilai anda adalah 2.0, kamu keren!')
    elif c == 'D':
        print('Nilai anda adalah 1.0, apakah sudah ada pikiran untuk pindah jurusan? ')
    elif c == 'E':
        print('Nilai anda adalah 0, niat kuliah nggak sih???')
    elif c == 'F':
        print('Inputan nilai yang anda masukkan tidak valid')
    else :
        print('Masukkan Dalam bentuk Alphabet')
except:
    print()
    

    