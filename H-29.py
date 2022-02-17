nama = input ("Nama : ")
jk = input ("Pria / wanita : ")
jk = jk.lower()
tanggal_lahir = int(input("Tanggal Lahir : "))
bulan_lahir = int(input("Bulan Lahir : "))
tahun_lahir = int(input ("Tahun Lahir : " ))

tahun_ini = 2021
bulan_ini = 12
hari_perbulan = 30

tahun = tahun_ini - tahun_lahir
bulan = bulan_ini - bulan_lahir 
hari = hari_perbulan - tanggal_lahir

if (jk =='wanita'):
    print ("Hay, mba",nama,"Tahun ini anda berusia",tahun,"Tahun,",bulan,"bulan,",hari,"hari.")

else :
    print ("Hay, mas",nama,"Tahun ini anda berusia",tahun,"Tahun,",bulan,"bulan,",hari,"hari.")
   

if (tahun <=25):
     print ("Apakah anda seorang Mahasiswa?")
       
elif (tahun <=60 ):
    print ("Apakah anda seorang pegawai atau pengusaha?")

else :
    print ("kemungkinan anda sudah pensiun")
