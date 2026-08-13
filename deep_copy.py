# import copy
# org=[['a1','standards',250],['a2','premium',500],['a3','recliner',700]]
# print(org)
# shallow_copy=copy.copy(org)
# shallow_copy[0][1]='premium'
# print(shallow_copy)
# print(org)
# deep_copy=copy.deepcopy(org)
# deep_copy[0][1]='luxary'
# print(deep_copy)
# print(org)
#
import copy
org={
    "user":'Archana',
    'seat':['A1','A2'],
    'seat_details':{'A1':'standard','A2':'premium'}
}
shallow=copy.copy(org)
shallow['seat'][1]='A3'
print(shallow)
deep_copy=copy.deepcopy(org)
deep_copy['seat_details']['A1']='luxary'
print(deep_copy)
print(org)


