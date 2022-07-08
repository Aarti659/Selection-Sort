List = []
num = int(input("Enter number of elements"))

print("Enter elements of List : ")

for data in range(num):
    b = int(input(" "))
    List.append(b)

    print("List is :", List)

for j in range(len(List)):
    for k in range(j+1, len(List)):
        if (List[j] > List[k]) :
            temp = List[j]
            List[j] = List[k]
            List[k] = temp

print("Sorted List is : ", List)

  
