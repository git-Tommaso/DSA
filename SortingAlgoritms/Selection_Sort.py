def Selection_Sort(my_list):
   for i in range(len(my_list)-1):
      min_index = i
      for j in range(i+1, len(my_list)):
         if my_list[j] < my_list[min_index]:
            min_index = j
      if min_index != i:
         temp = my_list[i]
         my_list[i] = my_list[min_index]
         my_list[min_index] = temp
   return my_list

print(Selection_Sort([5, 2, 9, 1, 5, 6]))