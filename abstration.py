from abc import abstractmethod, ABC
# # class Whatsapp(ABC):
# #     @abstractmethod
# #     def send(self):
# #         pass
# # class SendPhoto(Whatsapp):
# #     def send(self):
# #         print("Compressing image..")
# #         print("Encrypting image..")
# #         print("Decrypting image..")
# #         print("Image sent!")
# # class SendText(Whatsapp):
# #     def send(self):
# #         print("Encrypting text..")
# #         print("Decrypting text..")
# #         print("Text sent!")
# # photo = SendPhoto()
# # photo.send()
# # text = SendText()
# # text.send()
# #
# #
# # class Instagram(ABC):
# #     @abstractmethod
# #     def post(self):
# #         pass
# #     @abstractmethod
# #     def likes(self):
# #         pass
# #     @abstractmethod
# #     def comment(self):
# #         pass
# # class Story(Instagram):
# #     def post(self):
# #         print('setting timer for 24hr')
# #         print("add stickers, add music, tag people, repost")
# #     def likes(self):
# #         print("showing top 2 liked profiles..")
# #     def comment(self):
# #         print("showing top 2 recent comments..")
# #
# # class ImagePost(Instagram):
# #     def post(self):
# #         print("No timer!!")
# #         print("Shareable to other apps..")
# #     def likes(self):
# #         print("display liked by.. notification")
# #         print("show likes count")
# #         print("show 3-4 icons of people who liked")
# #     def comment(self):
# #         print("statically show 2-3 comments..")
# # story1 = Story()
# # story1.post()
# # story1.likes()
# # image1 = ImagePost()
# # image1.likes()
# # image1.post()
#
from abc import abstractmethod, ABC
# class  Payment(ABC):
#     @abstractmethod
#     def pay(self):
#         self.amount=amount
# class UPI(Payment):
#     def pay(self,paid):
#         super().__init__(amount)
#         print("upi is done throught the scanner or phonepay number")
#         self.balance=amount-paid
#         print("Your Total Remaining amount is:  ",balance)
# # class CreditCard(Payment):
# #     def pay(self,name,year,number):
# #         if name==
# #         print("CreditCard payment is working")
# #         self.amount=amount
# #         print("your amount is paying through the creditcard")
# #         print(amount)
# # class Cash(Payment):
# #     def pay(self,amount):
# #         print("Your are paymenting through  the cash")
# #         self.amount=amount
# #         print("your total amount payable",amount)
# #
# payment1=UPI()
# payment1.pay(100,1000)


from abc import ABC,abstractmethod
# class PaymentGateway('ABC'):
#     @abstractmethod
#     def initiate(self,amount):
#         pass
#     @abstractmethod
#     def verify(self,transaction_id):
#         pass
#     @abstractmethod
#     def refund(self,transaction_id):
#         pass
# class RazorPay(PaymentGateway):
#     def initiate(self,amount):
#         print(f"initializing payment of Rs.{amount}via Razonpay")
#     def verify(self,transaction_id):
#         print(f"Verifying tranction id{transaction_id}")
#     def refund(self,transaction_id):
#         print(f"Refund initiated for transaction id:{transaction_id}")
# obj=PaymentGateway()

#
# class DataStorage(ABC):
#     def __init__(self,data=[]):
#         self.data=data
#     @property
#     @abstractmethod
#     def storagetype(self):
#         pass
#     @abstractmethod
#     def save(self,data):
#         pass
#     @abstractmethod
#     def load(self,key):
#         pass
#     @abstractmethod
#     def delete(self,key):
#         pass
# class FileStorage(DataStorage):
#     def save(self,data):
#         print(f"saving data in the file..{data}")
#         self.data.append(data)
#     def load(self,key):
#         print(f"Loading data with key..{key}")
#     def delete(self,key):
#         print(f"Deleting data with key..{key}")
#     @property
#     def storagetype(self):
#         return FileStorage._name_
# class MemoryStorage(DataStorage):
#     def save(self,data):
#         print(f"Saving data in memory space..{data}")
#         self.data.append(data)
#     def load(self,key):
#         print(f"Loading Data with key..{key}")
#     def delete(self,key):
#         print(f"Deleting data with key.{key}")
#     @property
#     def Storagetype(self):
#         return MemoryStorage._name_
# file=FileStorage()
# file.save("Hey!")
# print(file.storagetype)
# mem=MemoryStorage()
# mem.save("this is data!")
# print(mem.storagetype)
# print(file.data)


#
# from abc import ABC, abstractmethod
# class PaymentGateway(ABC):
#     @abstractmethod
#     def initiate(self, amount):
#         pass
#     @abstractmethod
#     def verify(self, transaction_id):
#         pass
#     @abstractmethod
#     def refund(self, transaction_id):
#         pass
# class RazorPay(PaymentGateway):
#     def initiate(self, amount):
#         print(f"Initiating payment of Rs. {amount} via RazorPay.")
#     def verify(self, transaction_id):
#         print(f"Verifying transaction id : {transaction_id}.")
#     def refund(self, transaction_id):
#         print(f"Refund initiated for transaction id: {transaction_id}.")
# class PayPal(PaymentGateway):
#     def initiate(self, amount):
#         print(f"Initiating payment of Rs. {amount} via PayPal")
#     def verify(self, transaction_id):
#         print(f"Verifying transaction id : {transaction_id}.")
#     def refund(self, transaction_id):
#         print(f"Refund initiated for transaction id: {transaction_id}")
# obj = PaymentGateway()

# class DataStorage(ABC):
#     def __init__(self, data = []):
#         self.data = data
#     @property
#     @abstractmethod
#     def storagetype(self):
#         pass
#     @abstractmethod
#     def save(self, data):
#         pass
#     @abstractmethod
#     def load(self, key):
#         pass
#     @abstractmethod
#     def delete(self, key):
#         pass
#
# class FileStorage(DataStorage):
#     def save(self, data):
#         print(f"Saving data in the file.. {data}")
#         self.data.append(data)
#     def load(self, key):
#         print(f"Loading data with key.. {key}")
#     def delete(self, key):
#         print(f"Deleting data with key..{key}")
#     @property
#     def storagetype(self):
#         return FileStorage.__name__
# class MemoryStorage(DataStorage):
#     def save(self, data):
#         print(f"Saving data in memory space.. {data}")
#         self.data.append(data)
#     def load(self, key):
#         print(f"Loading data with key.. {key}")
#     def delete(self, key):
#         print(f"Deleting data with key..{key}")
#     @property
#     def storagetype(self):
#         return MemoryStorage.__name__
# file = FileStorage()
# file.save("Hey!!")
# print(file.storagetype)
# mem = MemoryStorage()
# mem.save("This is data!!")
# print(mem.storagetype)
# print(file.data)

#
# class APBoard:
#     @property
#     @abstractmethod
#     def hallticket_no(self):
#         pass
# class SriChaitanya(APBoard):
#     @property
#     def hallticket_no(self):
#         #validation
#         return "21027026038"
# class Narayana(APBoard):
#     @property
#     def hallticket_no(self):
#         return "2345267238"
# alice = SriChaitanya()
# print(alice.hallticket_no)
# bob = Narayana()
# print(bob.hallticket_no)



# class User(ABC):
#     def __init__(self,name,pwd):
#         self.name=name
#         self.pwd=pwd
#     @abstractmethod
#     def register(self):
#         pass
# class Instagram(User):
#     def __init__(self,name,pwd):
#         super().__init__(name,pwd)
#     def register(self):
#         print(f"user{self.name} registered on instagram!")
# class Facebook(User):
#     def __init__(self,name,pwd):
#         self.pwd=pwd
#         super().__init__(name)
#
#     def register(self):
#         print(f"User{self.name}registered on facebook!")


from abc import ABC,abstractmethod
class Account(ABC):
    interest_rate=2
    def __init__(self,balance):
        self.__balance=balance
    @property
    def balance(self):
        pin=int(input("Enter Pin:"))
        if pin==1234:
            return self.__balance
        else:
            print("you have entered incorrect pin.")
    @abstractmethod
    def deposite(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def calculate_interest(self):
        pass
    @staticmethod
    def validate_amount(amount):
        return amount>0
    @classmethod
    def change_interest_rate(cls,interest_rate):
        cls.interest_rate=interest_rate
class SavingsAccount(Account):
    def deposite(self,amount):
        if self.validate_amount(amount)
            self.balance+=amount
            print("amount deposites successfuly")
        else:
            print("you have entered invalid amount")
    def withdraw(self,amount):
        if self.validate_amount(amount):
            self.balance-=amount
            print("amount withdraw successfily")
        else:
            print("you have entered invalid amount")
    def calculate_interest(self):
        return self.balance*2/100
class CurrentAccount(Account):
    def deposite(self,amount):
        if self.validate_amount(amount):
            self.balance+=amount
            print("amount deposited successfully")
