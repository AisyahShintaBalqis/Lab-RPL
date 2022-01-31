List = [1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12]
print("List: ")
print(List)
 

List.remove(9)
List.remove(1)
print("\nList setelah 2 elemen di hapus: ")
print(List)
 

for i in range(4, 5):
    List.remove(i)
print("\nList: ")
print(List)
