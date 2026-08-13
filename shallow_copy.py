import copy
list_org=[['hii','hello'],['ramesh','suresh'],['hru','bye']]
# shallow_cpy=copy.copy(list_org)
# shallow_cpy[0][0]='archana'
# print(list_org)
# print(shallow_cpy)
# print(id(shallow_cpy))
# print(id(list_org))
# print(id(list_org[0]))
# print(id(shallow_cpy[0]))

#deep copy
deep_cpy=copy.deepcopy(list_org)
deep_cpy[1][1]='tea'
print(list_org)
print(deep_cpy)