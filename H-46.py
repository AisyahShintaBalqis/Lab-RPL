List = []
print("Initial blank List: ")
print(List)
 

List.append(1)
List.append(2)
List.append(4)
print("\nPenambahan 3 elemen")
print(List)
 

for i in range(1, 4):
    List.append(i)
print("\npenambahan elemen 1-3 : ")
print(List)
 

List.append((5, 6))
print("\nPenambahan Tuple: ")
print(List)
 

List2 = ['Manggis', 'Mangga']
List.append(List2)
print("\nPenambahan List : ")
print(List)
