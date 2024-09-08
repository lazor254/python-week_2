my_list = []

# appending the values
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# inserting 15 at second position knowing counting starts from 0
my_list.insert(1, 15)
print(my_list)

my_list2 = [50, 60, 70]
print(my_list2)

#extending he list and printing the output
my_list.extend(my_list2)
print(my_list)

#removing the last element
my_list.pop()
print(my_list)
 
 #sorting in ascending order
my_list.sort()
print(my_list)

position = my_list.index(30)
print(position)

# output
""" 
[10, 20, 30, 40]
[10, 15, 20, 30, 40]
[50, 60, 70]
[10, 15, 20, 30, 40, 50, 60, 70]
[10, 15, 20, 30, 40, 50, 60]
[10, 15, 20, 30, 40, 50, 60]
3
"""