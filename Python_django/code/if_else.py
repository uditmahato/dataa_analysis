# if-else example
# if-else is a conditional statement in python.
# if-else is used to execute one of two statements based on a condition.
#example
# if condition:
#     statement
# else:
#     statement

from multiprocessing.sharedctypes import Value


salary = int(input("Enter your salary: "))
if salary > 10000:
    print("You are a rich person")
else:
    print("You are not a rich person")


#elif
# elif is used to execute one of more statements based on a condition.
# elif is used to execute one of more statements based on a condition.  It is used after if.

Value = int(input("Enter your value: "))
if Value > 0:
    print("Value is positive")
elif Value < 0:
    print("Value is negative")
else:
    print("Value is zero")

# if else boolean
# if else boolean is used to execute one of two statements based on a condition.
# if else boolean is used to execute one of two statements based on a condition.  It is used after if.
# example
# if condition: 
#     statement
# else:
#     statement

#pass example
# pass is used to do nothing.
#code
x=False
if x==True:
    pass
else:
    print("This is not true")
