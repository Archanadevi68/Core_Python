# class PasswordUtils:
#     @staticmethod
#     def is_strong(password):
#         digit_check=False
#         upper_check=False
#         for i in password:
#             if i.isdigit():
#                 digit_check=True
#             if i.isupper():
#                 upper_check=True
#         return len(password)>=8 and digit_check and upper_check
#     @staticmethod
#     def generate_hint(password):
#         print(password[0:2]+"*")
#     @staticmethod
#     def validate_email(email):
#         return '@' in email and '.' in email
# pwd='ABCWXYSS@123'
# # PasswordUtils.generate_hint(pwd)
# print(PasswordUtils.validate_email("archana043@gmail.com"))
# print(PasswordUtils.is_strong(pwd))


class Libary:
    libary_name="py-21"
    def __init__(self,book_list,member_name):
        if member_name=="":
            raise ValueError("Name Cannot be empty.")
        else:
            self.book_list=book_list
            self.member_name=member_name
    def add_book(self,title):
        if Libary.is_valid_title(title):
            self.book_list.append(title)
            print("New book added sucessfuly!!")
        else:
            print("enter a valid title")
    @classmethod
    def create_guest(cls):
        return Libary([],"Guest")
    @staticmethod
    def is_valid_title(title):
        return title!='' and title!=None



user1 = Libary(["ABC", "DEF"], "Guest")
# user2 = Library(["LMN", "OPQ"], "User2")
# user1.add_book("PQL")
# print(user1.book_list)
print(Libary.libary_name)