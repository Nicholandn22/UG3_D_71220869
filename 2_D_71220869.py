a = input('Masukkan Plat Nomor : ').lower().split()

try:
   b = int(a[1])
   if b <= 3000:
    print('Plat nomor tersebut diperuntukkan untuk mobil')
   elif b <= 4000:
    print('Plat nomor tersebut diperuntukkan untuk motor')
   elif b < 5000:
    print('Plat nomor tersebut diperuntukkan untuk angkutan umum')
   elif b > 5000:
    print('Plat nomor tidak terindikasi ketiga angkutan tersebut')
except:
    print('Plat Nomor Tidak Terindikasi, setelah kode daerahh harus berupa nomor kendaraan')