my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
new_list1 = sorted(my_list)
print(new_list1)
new_list2 = sorted(my_list, reverse=True)
print(new_list2)
new_list3 = new_list1[1::2]
print(new_list3)
new_list4 = new_list1[0::2]
print(new_list4)
for i in my_list:
    if i%3==0:
        print(i)
