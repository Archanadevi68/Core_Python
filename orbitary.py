# def add(*args):
#     print(args)
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
# add(10,20,30)
# add(10,20)


# def order_details(**details):
#     for key,value in details.items():
#         print("key:",key,"value:",value)
# order_details(**{"a":1,"b":2,"c":3})


# def register_patient(**args):
#     for key, value in args.items():
#         print(key, value)
# register_patient(**{'name':input(),'age':int(input()),'symtomps':input(),'doctor_sigh':input()})

# def product(*args):

#     s=1
#     for i in args:
#         s*=i
#     return s
# print(product(7,8,9,10,11))

# def display_tags(**kwargs):
#     for key,value in kwargs.items():
#         print('key:',key,'value:',value)
# display_tags(**{'name':'archana','batch':21})

# 1.create a python application to develop a hospital building system create functions like calculate bill with orbitary positional arguments called charges.
# 2.create another function applay incurence with orbitary keyword word arguments and
# 3.create a function add taxes with orbitary  keyword arguments the programme should accept multiple charges applay incurence reduction then add taxes

def hospital_building(*calculate):
    c=0
    for i in calculate:
        c+=i
    print("total hospital bill is:",c)
    return c
# hospital_building( 20000,50000,1000)

def incurence(**discount):
    x=0
    for key,value in discount.items():
        x+=value
    print("total incurence amount is:",x)
    return x

# incurence(**{'refund':2000,'lic':15000,'sukanya':2000})
def tax(**tax_amount):
    s=0
    for key,value in tax_amount.items():
        s+=value
    # return s
    print("total tax amount is:",s)
    return s
# tax(**{'gst':2000,'sgst':500})

print("The Total Bill is:",
      hospital_building(20000, 50000, 1000)
      - incurence(refund=2000, lic=15000, sukanya=2000)
      + tax(gst=2000, sgst=500))
# def cbill(*args):
#     bill=0
#     for i in args:
#         bill+=i
#     return bill
# def insurance(**disc):
#     discount =0
#     for key,value in disc.items():
#         discount+=value
#     return discount
# def add_taxes(**tax):
#         taxi=0
#         for key,value in tax.items():
#             taxi+=value
#         return taxi
# b=cbill(900,1800,1000)
# i=insurance(lic=20000,star=1000,mega_sale=1000)
# t=add_taxes(hospital_rent=10000,medicine=5000,treatment=50000)
# a=t-i+b
# print(a)


def calculate_total(*prices):
    bill=0
    for i in prices:
        bill+=i
        return bill
def apply_discount(amount):
    if bill > 1500 :
        discount=(10/100)* bill
        return amount - discount
    else :
        return amount
def final_bill(amount,**charges):
    final_amount=0
    for key,value in charges.items():
        final_amount+=value
      return amount+final_amount
print(final_bill(apply_discount(calculate_total(200,500,300,8000),gst=200,)))



#10/7/2026

def total_bill(charges):
    s=0
    for i in charges:
        s+=i
    return s
def incurence(amount,**discount):
    x=0
    for key,value in discount.items():
        x+=value
    return amount-x







