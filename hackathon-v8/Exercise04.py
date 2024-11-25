my_list = [1, 2, 3, 4, 5]
small_num = [0]

for i in my_list:
    if small_num < my_list:
        small_num = my_list
        print(small_num)