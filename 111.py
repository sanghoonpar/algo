list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1)
print(list2)
list1.append(list2)
list2.extend(list1)
print(list1)
print(list2)
print(list1+list2)