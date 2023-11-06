def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value=a_list[index]
        position=index
        while position > 0 and a_list[position-1] > current_value:
            a_list[position]=a_list[position-1]
            position=position-1
            a_list[position]=current_value

a_list=[27, 10, 15, 3, 8, 2]
insertion_sort(a_list)
print(a_list)