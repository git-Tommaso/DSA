def item_in_common(list1, list2):
   # Create a dictionary to store items from the first list
   my_dict = {}
   for i in list1:
      my_dict[i] = True  # Mark each item as present in the dictionary

   # Check if any item in the second list exists in the dictionary
   for j in list2:
      if j in my_dict:  # If found, return True
         return True
      
   return False  # Return False if no common item is found

list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2)) # True