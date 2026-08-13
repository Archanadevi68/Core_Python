def calculate_bill(*charges):
    total = 0
    for charge in charges:
        total += charge
    return total
def apply_discount(*amount):
    total_bill = 0
    for charges in amount:
        total_bill += charges
    if total_bill > 1500:
        total_bill = total_bill - (total_bill * 0.1)
    return total_bill
def final_bill(**details):
    total_bill = 0
    for key, value in details.items():
        print(key,":",value)
        total_bill += value
    return total_bill
# print(final_bill(total_bill = apply_discount(calculate_bill(int(input("enter amt 1:")),
#                int(input("enter amt 2:")),
#                int(input("enter amt 3:")))),
#            shipping_charges = 250,
#            packaging_charges = 250,
#            international_tax = 300,
#            GST = 100,
#            SGST = 50))



#order of all args
# mandatory, default args, arbitrary positional, arbitrary keyword
def message(sender, receiver, app = "whatsapp", *msgs, **reactions):
    print("Sender:",sender)
    print("Receiver:",receiver)
    print("You're using app:", app)
    for msg in msgs:
        print("Message:", msg)
    for reaction, emoji in reactions.items():
        print("Reactions:",reaction, "Emoji:", emoji)
# message("A", "B", "instagram", "hey", "how are you?", "wyd?", laugh = "laughing emoji", curious = "curious emoji")


def swiggy(customer_name, order_type = "regular", *items, **details):
    print("Hi !", customer_name)
    print("order type :", order_type)
    total_bill = 0
    print("Your order details are:")
    for item in items:
        print(item[0], "Rs.", item[1])
        total_bill += item[1]
    print("Additional Details:")
    for detail,about in details.items():
        print(detail, ":", about)
    print("Total Bill: Rs. ", total_bill)

swiggy("Archana", "Swiggy One",
       ["Burger", 250],["Fries", 99],["Chips", 59],
       ["Cola", 79],
       payment_mode = "UPI",
       address = "Road no 1, KPHB",
       add_ons= ["ketchup", "mustard"])

# swiggy("Sai", "Swiggy Black",
#        ['Chicken Biryani', 250],['cola', 79], ['Gulab Jamun', 99],
#        payment_mode = "UPI",
#        cooking_instructions = "Make it a bit spicy.",
#        address = "Road no 2, KPHB")

# def describe_person(name, *hobbies):
#     print("Hi ! My name is ", name)
#     print("My hobbies are : ", end = " ")
#     for hobby in hobbies:
#         print(hobby, end = " ")

# describe_person("Latha", "Reading Books", "Travelling to the Mountains", "singing")

# def f(*args):
#     print(type(args))
# f(10,20,30)

# def html_tags(tag, **attributes):
#     print("<", tag, end = " ")
#     for attribute in attributes:
#         print(attribute," = ", attributes[attribute], end = " ")
#     print(">")
#
# html_tags("'a'", style = "italic bold", border = "2px black",
#           height = "100%", width = "100%" )
#
# print(type(html_tags))
# x=html_tags
# x("'img",style='bold',border="2px black",height="100%",width="100%")

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# # calculate=[add,sub,mul,div]
# # print(calculate[0](10,20))
#
# operator={
#     '+':add,
#     '-':sub,
#     '*':mul,
#     '/':div
# }
# op=input()
# print(operator[op](20,30))


# def squre(a):
#     return a**2
# def twice(squre,value):
#     return squre(squre(value))
# print(squre(2))
# print(twice(squre,2))


# def cube(a):
#     return a**3
# def twice(cube,value):
#     return cube(cube(value))
# # print(cube(2))
# print(twice(cube,2))

# def html_tag(tag,**args):
#     print("<",tag,">",end=" ")
#     for arg in args:
#         print(arg,"=",args[arg],end=" ")
#         print("</h1>")
# html_tag("h1",style="italic",border='20 px')
#
