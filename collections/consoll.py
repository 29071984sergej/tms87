my_list = [1, 2, 3, 4, 5, 6, 7]
my_list.append('hello')
print(my_list)
my_list.pop(0)
print(my_list)
my_list[0] = ("Word")

print(my_list)
my_list.remove("Word")
print(my_list)
print(my_list[::-1])
      
my_list = [1, 2, 3, 4, 5, 6, 7]

my_list2 = [8, 9, 10, 11, 12]
print(my_list, my_list2)
my_list2.extend(my_list2)
print(my_list)
my_list.insert(4, 123)
print(my_list)

print(len(my_list))
