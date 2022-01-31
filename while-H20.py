matkul = ['Matematika Dasar', 'Matematika Diskrit', 'Aljabar ', 'Algoritma', 'Pengantar Sistem Informasi', 'Struktur Data', 'Multimedia', 'PBO']

# jika indeks pada matkul adalah bilangan genap maka akan di skip
# dan i lebih dari 0
i = 0
while i < len(matkul):
  i += 1
  if i % 2 == 0 and i > 0:
    print('skip')
    continue

  # tidak dieksekusi ketika continue dipanggil
  print(matkul[i])
