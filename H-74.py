angka=1
while(angka<=10):
    print(angka)
    angka +=1
else:
    print("num sudah mencapai %d" %(angka))

for i in range(1, 15):
    if(i%15==0):
        break
    print(i)
else:
    print("ini tidak akan dicetak karena perulangan dihentikan oleh break bukan karena kesalahan kondisi")
