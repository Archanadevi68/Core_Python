# class student:
#     def __init__(self,age):
#         if age>=18:
#             self.age=age
#         else:
#             raise ValueError("age is below 18")
# s1=student(18)
# # print(s1)
from multiprocessing import process


class BankAccount:
    bank_name="Abc"
    def __init__(self,account_holder,account_number,balance):
        if balance>0:
            self.age=balance
            self.account_holder=account_holder
            self.account_number=account_number
            # self.balance=balance
        else:
            self.age=0
            self.account_holder = account_holder
            self.account_number = account_number
            # self.balance=0
b1=BankAccount('archana',12345678,500)
b2=BankAccount('arjun',236789235,-1)
print(b2.__dict__)
print(b2.bank_name)


# class Employee:
#     company='TechCorp'
#     employee_count=0
#     def __init__(self,name,department,salary,experience):
#         if salary>0 and experience>0:
#             if experience>5:
#                 self.bonus=(salary*15)//100
#             elif experience>=3:
#                 self.bonus=(salary*10)//100
#             else:
#                 self.bonus=(salary*5)//100
#             self.name = name
#             self.department = department
#             self.salary = salary
#             self.experience = experience
#             Employee.employee_count += 1
#             self.employee_id = Employee.employee_count
#             final_salary=salary+self.bonus
#             self.pay_details = {
#                 "name": name,
#                 "salary": self.salary,
#                 "experience": experience,
#                 "bonus": self.bonus,
#                 "final_salary": final_salary
#             }
#
# e1 = Employee("Archana", "IT", 50000, 6)
# e2 = Employee("Ravi", "HR", 40000, 4)
# e3 = Employee("Priya", "Finance", 30000, 2)
# # print(e1.__dict__)
# # print(e2.__dict__)
# # print(e3.__dict__)
# e1.pay_details["bonus"]= 3345
# print(e1.__dict__)
#


# class MobilePurchase:
#     store_name="Smart Mobile"
#     Purchase_count=0
#     def __init__(self,customer,brand,price,storage,quality):
#         if price>0 and quality>0 and storage in (64,128,256,512):
#             self.customer=customer
#             self.brand=brand
#             self.price=price
#             self.storage=storage
#             MobilePurchase.Purchase_count += 1
#             self.Purchase_count = MobilePurchase.Purchase_count
#             total=price*quality
#             if total>=50000:
#                 discount=10*total//100
#             else:
#                 discount=5*total//100
#             price=total-discount
#             self.purchase_detalis={
#                 "name":customer,
#                 "brand":brand,
#                 "price":price,
#                 "storage":storage
#             }
# r1=MobilePurchase('archana','samsung',20000,512,1)
# print(r1.__dict__)





# class product:
#     store="ShopEasy"
#     def __init__(self,name,price,qaulity):
#         self.name=name
#         self.price=price
#         self.qaulity=qaulity
#         self.product_details={
#             "product_name":name,
#             "price":price,
#             "quality":qaulity
#         }
# e1=product('archana',150000,2)
# e2=product('priya',500000,1)
# e1.price=50000
# e1.product_details['price']=200000
# print(e1.__dict__)




# class vote:
#     def __init__(self,age):
#         if isinstance(age, int):
#             self.age=age
#         else:
#             print("you've entered a wrong value, so pls enter an integer value")
# e1=vote('hii')
# print(e1.__dict__)
# print(isinstance(e1,vote))
# print(isinstance(e1,int))
# print(type(e1) is vote)



# class zomato:
#     names=[]
#     cupon='cu90n'
#     discount=10
#     id=0
#     def __init__(self,r_name,r_id):
#         self.name=r_name
#         self.r_id=r_id
#         zomato.id+=1
#         self.menu={
#             'briyani':[{'chicken':200,'mutton':400,'fish':300,'prawns':500}],
#             'desserts':[{'icecream':100,'appricot':150,'gulabjam':50}],
#             'soft_drinks':[{'thumps up':25,'marinda':25,'lemoca':25,'sprit':'25'}]
#         }
#
#
# r1=zomato('pradise',1)
#
# print(r1.__dict__)



