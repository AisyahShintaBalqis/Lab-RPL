print ("======================Hotel AAA==================")

print ("Kamar yang tersedia :")
print (" VVIP ")
print (" VIP ")
print (" Ekonomi ")

print ("Silahkan Melakukan Registrasi\n")

nama = input ("Nama Lengkap : " )
jk = input ("Jenis Kelamin (L/P) : ")
jk = jk.lower()
kelas = input ("Kategori Kamar : " )
kelas = kelas.lower()
jumlah = int(input ("Jumlah Hari : " ))


vvip = 3000000
vip = 2500000
ekonomi = 2000000

if kelas == "vvip" :
    harga = vvip * jumlah
    if jk == 'L' :
        print ("Hay mas",nama,"Silahkan melakukan pembayaran senilai Rp. ",harga)
    else :
        print ("Hay Mba",nama,"Silahkan melakukan pembayaran senilai Rp. ",harga)


elif kelas == "vip" :
    harga = vip * jumlah
    if jk == 'L' :
        print ("Hay mas",nama,"Silahkan melakukan pembayaran senilai Rp. ",harga)
    else :
        print ("Hay Mba",nama,"Silahkan melakukan pembayaran senilai Rp. ",harga)

elif kelas == "ekonomi" :
    harga = ekonomi * jumlah
    if jk == "L" :
        print ("Hay mas",nama,"Silahkan melakukan pembayaran senilai Rp. ",harga)
    else :
        print ("Hay Mba",nama,"Silahkan melakukan pembayaran senilai Rp. ",harga)

else :
    print ("Hay Mba",nama,"Maaf Kategori kamar yang anda inputkan tidak tersedia")
