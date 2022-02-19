gaji = int (input("Gaji anda : "))
profesi = input("Pekerjaan anda : ")
profesi=profesi.lower()

if gaji >=3000000:    
    potongan = gaji - (gaji * 5/100)    
    if profesi == 'PNS':
        gajibersih = potongan - (potongan * 5/100)
        print ("Gaji Bersih yang anda terima: ",gajibersih)

    else:
        print ("Gaji Bersih yang anda terima: ",potongan)
        
        
elif gaji >=5000000:
    potongan = gaji - (gaji * 10/100)    
    if profesi == 'PNS':
        gajibersih = potongan - (potongan * 5/100)
        print ("Gaji Bersih yang anda terima: ",gajibersih)

    else:
        print ("Gaji Bersih yang anda terima: ",potongan)

else :
    print ("Gaji anda tidak di kenakan potongan pajak")
