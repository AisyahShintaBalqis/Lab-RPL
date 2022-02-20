tb = [190, 160, 180, 170, 150]

print("Daftar Tinggi Badan : \n",tb)

#fungsi extend
tb1 = [130,110]
tb.extend(tb1)
print("\nDaftar Tinggi Badan : \n", tb)

#fungsi reverse
tb.reverse()
print("\nDaftar Tinggi Badan : \n", tb)

#fungsi sort
tb.sort()
print("\nDaftar Tinggi Badan (sort) : \n", tb)

#fungsi Max
print("\nTinggi Badan Tertinggi : \n", max(tb))

#Fungsi  min
print("\nTinggi Badan Terpendek : \n", min(tb))

#fungsi Sum
print("\nJika semua Tinggi Badan di jumlahkan : \n", sum(tb))
