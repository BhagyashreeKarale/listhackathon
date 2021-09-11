# Iterate over both the values in a list and their indices
# grocery_list = ['flour','cheese','carrots']
# Output: 
# #=> 0: flour
# #=> 1: cheese
# #=> 2: carrots


grocery_list = ['flour','cheese','carrots']
count=0
for item in grocery_list:
    print(count,":",item)
    count=count+1
