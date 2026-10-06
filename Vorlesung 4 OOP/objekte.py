# class str -> Call by value
'''
my_string1 = "Hi"
my_string2 = my_string1
my_string1 += " students"

print(my_string2) 
print(my_string1) 
'''

# class list -> Call by reference
numbers_list1 = [2, 3, 4]
print(id(numbers_list1))
print(type(numbers_list1))


numbers_list2 = numbers_list1
numbers_list1.append(5)

print(numbers_list2) 
print(numbers_list1) 

