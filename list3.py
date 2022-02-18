
print ("=================Kemana-Kemana===============")


Destinasi= []

tujuan=input("Tambahkan Tujuan Anda : ")
tujuan=tujuan.lower()


if tujuan == 'makassar' :
    Destinasi.append('makassar')
elif tujuan == 'palu' :
    Destinasi.append('Palu')

elif tujuan == 'bali' :
    Destinasi.append('bali')

elif tujuan == 'jakarta' :
    Destinasi.append('jakarta')

elif tujuan == 'jogja' :
    Destinasi.append('jogja')
    
else :
    print ("Maaf, Tujuan anda tidak dapat di tambahkan ! ")
    

print ("Daftar Tujuan Anda : ",Destinasi)
    






