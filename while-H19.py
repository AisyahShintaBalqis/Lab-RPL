angka = int(input('Masukkan angka ganjil lebih kecil dari 50: '))

while angka % 2 != 1 or angka >= 50:
  angka = int(input('Salah, masukkan lagi: '))

print('Benar')
