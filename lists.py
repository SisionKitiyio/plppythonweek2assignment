my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1,15)#insert 15 at index 1 the second position

my_list.extend([50, 60, 70])

my_list.pop()#remove the last element 70

my_list.sort()
index_of_30 = my_list.index(30)#find and print the index of the value 30 in my list

print("Updated list:", my_list)
print("Index of 30:", index_of_30)

