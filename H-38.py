
#sorting list
a =[7,9,6,4,7,8]
print("A = ",a)

b = a
print("B = ",b)

#membalik urutan list
a.reverse()
print ("B = ",b)

x = []

for i in (a):
    if i % 2 == 0 and i >= 1:
        x.append(i)

    else:
        x.append("")

x.reverse()
b = x

print("B = ",b)
    
