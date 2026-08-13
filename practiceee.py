def intro(name, city, hobby):
    print("My name is", name)
    print("I live in", city)
    print("My hobby is", hobby)
# intro("Abhilash", "Vijaywada", "Watching movies")
# intro(hobby = "Watching movies", name = "Abhilash", city = "Vijaywada")

def sub(a,b):
    return a - b
# print(sub(10,3))
# print(sub(3,10))
# print(sub(b = 3, a = 10))

def bio(firstname, lastname, age):
    print("My name is "+firstname +" "+lastname)
    print("I am "+str(age)+" years old.")
# bio("Rana", "Daggubati", 30)
# bio("30", "Daggubati", "Rana")
# bio(age = 30, firstname="Rana", lastname="Daggubati")

def send_mail(to, subject, body):
    print("To :", to)
    print("Subject :", subject)
    print(body)
# send_mail(body = "Requesting update for the project deadline to 30th of July 2026.", to = "manager@office.in", subject = "Rescheduling Deadline for Upcoming Project")
#
# def create_profile(username, email, age, password, app ):
#     print("Hi", username)
#     print("You are using ", app)
#     print("Your email address is", email)
#     print("Your password is ", password)
#     print("Your age :", age)
# create_profile("user@101", "user@gmail.com", app = "insta", password ="welcome@123", age = 23)

#
# def book_ticket(name, pickup, drop, tickets):
#     print("Hi", name)
#     print("Pick up:", pickup)
#     print("drop:", drop)
#     print("tickets:", tickets)
# book_ticket(tickets = 2, drop = "Mumbai", name = "Alice", pickup = "Delhi")
# book_ticket("alice", "mumbai", "delhi", 3)


def greeting(age, name = "user"):
    print("Hello, " + name)
    if age >= 18 :
        print("You're eligible to vote")
    else:
        print("You are not eligible to vote")
# greeting(19)
# greeting(19, "Archana")
greeting(name = "Archana", age = 20)
greeting(age = 20)


