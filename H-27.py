Buku = {
    'Judul': 'Laskar Pelangi',
    'penulis': "Andrea Hirata",
    'kategori': {'Novel':1,'Sastra':2}
 }
print ("Judul awal:",Buku['Judul'])
Buku['Judul'] = 'Sang Pemimpi'
print("setelah di ubah :",Buku['Judul'])
print ("penulis:",Buku['penulis'])
Buku['kategori']['Novel'] = 5
print ("kategori Novel: ",Buku['kategori']['Novel'])
print ("kategori Sastra: ",Buku['kategori']['Sastra'])

