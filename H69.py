def halo(nama):
    print ("Halo !",nama)

def cetak_maksimal(a, b):
    if a > b:
        print ("merupakan nilai maksimal",a)
    elif a == b:
        print ("sama dengan",(a, b))
    else:
        print ("merupakan nilai maksimal",b)

halo('AiSyah')  
halo('Shinta')  

cetak_maksimal(10, 7)

x = 9
y = 90

cetak_maksimal(x, y)
