class PasswordUtils:
    @staticmethod
    def is_strong(password):
        digit_check=False
        upper_check=False
        for i in password:
            if i.isdigit():
                digit_check=True
            if i.isupper():
                upper_check=True
        return len(password)>=8 and digit_check and upper_check
    @staticmethod
    def generate_hint(password):
        print(password[0:2]+"*")
    @staticmethod
    def validate_email(email):
        return '@' in email and '.' in email
pwd='ABCWXYSS@123'
# PasswordUtils.generate_hint(pwd)
print(PasswordUtils.validate_email("archana043@gmail.com"))
print(PasswordUtils.is_strong(pwd))