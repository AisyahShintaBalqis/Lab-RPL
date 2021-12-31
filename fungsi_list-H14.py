tahun_lahir = [2000, 2001, 2002, 2003, 2004, 2005, 2006]


print("Daftar Tahun Lahir : \n",tahun_lahir)

#fungsi len
print("\nJumlah data Tahun Lahir : \n", len(tahun_lahir))

#fungsi count
print("\nJumlah data lahir tahun 2001) : \n", tahun_lahir.count(2001))

#fungsi append
print("\nMenambahkan data Tahun Lahir : ")
tahun_lahir.append(1999)
tahun_lahir.append(1998)
print("Daftar Tahun Lahir : ",tahun_lahir)

#fungsi index
print("\nTahun Lahir 2005 ada di urutan ke : \n", tahun_lahir.index(2005))

#fungsi insert
tahun_lahir.insert(2001,1999)
print("\nTambah data Tahun Lahir List : \n", tahun_lahir)

#fungsi pop
tahun_lahir.pop()
tahun_lahir.pop()
print("\nTahun Lahir : \n",tahun_lahir)

#fungsi remove
tahun_lahir.remove(2001)
tahun_lahir.remove(2003)
print("\nData Tahun Lahir : \n", tahun_lahir)

#fungsi extend
tahun_lahir2 = [2011,2012]
tahun_lahir.extend(tahun_lahir2)
print("\nList Nilai (extend : \n", tahun_lahir)

#fungsi reverse
tahun_lahir.reverse()
print("\nData Tahun Lahir : \n", tahun_lahir)

#fungsi sort
tahun_lahir.sort()
print("\nData tahun Lahir (sort) : \n", tahun_lahir)

#fungsi Max
print("\nTahun Lahir Termudah : \n", max(tahun_lahir))

#Fungsi  min
print("\nTahun Lahir Tertua : \n", min(tahun_lahir))

#fungsi Sum
print("\nJika semua Tahun Lahir di jumlahkan : \n", sum(tahun_lahir))
