# from abc import abstractmethod, ABC
# class Whatsapp(ABC):
#     @abstractmethod
#     def send(self):
#         pass
# class SendPhoto(Whatsapp):
#     def send(self):
#         print("Compressing image..")
#         print("Encrypting image..")
#         print("Decrypting image..")
#         print("Image sent!")
# class SendText(Whatsapp):
#     def send(self):
#         print("Encrypting text..")
#         print("Decrypting text..")
#         print("Text sent!")
# photo = SendPhoto()
# photo.send()
# text = SendText()
# text.send()
#
#
# class Instagram(ABC):
#     @abstractmethod
#     def post(self):
#         pass
#     @abstractmethod
#     def likes(self):
#         pass
#     @abstractmethod
#     def comment(self):
#         pass
# class Story(Instagram):
#     def post(self):
#         print('setting timer for 24hr')
#         print("add stickers, add music, tag people, repost")
#     def likes(self):
#         print("showing top 2 liked profiles..")
#     def comment(self):
#         print("showing top 2 recent comments..")
#
# class ImagePost(Instagram):
#     def post(self):
#         print("No timer!!")
#         print("Shareable to other apps..")
#     def likes(self):
#         print("display liked by.. notification")
#         print("show likes count")
#         print("show 3-4 icons of people who liked")
#     def comment(self):
#         print("statically show 2-3 comments..")
# story1 = Story()
# story1.post()
# story1.likes()
# image1 = ImagePost()
# image1.likes()
# image1.post()

from abc import abstractmethod, ABC
class  Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(Payment):
    def pay(self,amount,balance):
        self.balance=balance
        print("upi is done throught the scanner or phonepay number")
        self.amount=amount
        balance-=amount
        print("Your Total Remaining amount is:  ",balance)
class CreditCard(Payment):
    def pay(self,name,year,number):
        if name==
        print("CreditCard payment is working")
        self.amount=amount
        print("your amount is paying through the creditcard")
        print(amount)
class Cash(Payment):
    def pay(self,amount):
        print("Your are paymenting through  the cash")
        self.amount=amount
        print("your total amount payable",amount)

payment1=UPI()
payment1.pay(100,1000)