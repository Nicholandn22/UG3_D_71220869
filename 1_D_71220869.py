a = input('Masukkan nilai curah hujan : ')
a = float(a)
print('Curah hujan ekstrem') if a > 100 else (print('Curah hujan lebat')if a > 50 else(print('Curah hujan sedang')if a > 20 else (print('Curah hujan ringan') if a > 0.5 else(print('Cuaca Terang/Berawan'))))) 