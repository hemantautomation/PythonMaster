my_list = [10,11,12,13,14,15]

odd_number = list(filter(lambda x: x%2 == 1 , my_list))
print(odd_number)


even_number = list(filter(lambda x: x%2 == 0 , my_list))
print(even_number)