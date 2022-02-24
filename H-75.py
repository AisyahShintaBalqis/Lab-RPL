angka=1
while(angka<=10):
    print(angka)
    angka +=1
else:
    print("num sudah mencapai %d" %(angka))

for i in range(100):
    if(i%2==1):
        continue
    print(i)
