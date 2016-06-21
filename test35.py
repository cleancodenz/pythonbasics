# in operator
#it can be applied in list, dictionary, Tuples, and strings


my_list = [1, 3, 4, 5, 6]
my_dict = {"S": "Small", "M": "Medium", "L": "Large", "XL": "X-Large"}
my_tuple = (10, 13, 15, 17, 11)
name = "Elvis Presley"
list_included = 1 in my_list
dict_included = "S" in my_dict
tup_included = 11 in my_tuple
string_included = 'vi' in name
 
print(list_included)
print(dict_included)
print(tup_included)
print(string_included)

list_not_included = 1 not in my_list

print(list_not_included)

