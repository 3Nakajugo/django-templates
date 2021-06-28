def remove_duplicates(duplicates_list):
  # print(duplicates_list)
  non_duplicates=[]
  for item in duplicates_list:
    if item not in non_duplicates:
      non_duplicates.append(item)
  
  return non_duplicates
  

data = input()
duplicates_list = data[1:-1].split(',')
 
print(remove_duplicates(duplicates_list))