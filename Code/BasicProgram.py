# display a person name, age and address in 3 diffrent lines

name = "Pratiksha Shinde"
Age = 22
Address = "Bavdhan, Pune Maharashtra"

print(name)
print(Age)
print(Address)

# To swap two variables
x = 23
y = 20

temp = x
x = y
y = temp

print("x: ",x)
print("y: ", y)
# method 2
x,y = y,x
print("swap using method 2 i.e Shift left and right")
print("x: ",x)
print("y: ",y)

# A program to convert Float into Interger
num1 = 3.234
print("float num : ",num1)

num_into_int = int(num1)
print("interger num : ",num_into_int)

# Take a details from a student for ID card and then print it in diff line
stu_name = input("enter your name:")
stu_age = int(input("enter your age:"))
class_name = input("enter your class:")

print(stu_name)
print(stu_age)
print(class_name)

# write a program to take an input as integer and convert it into float
number = int(input("enter your number:"))
print("number type integer: ",number)

number_float = float(number)
print("number covert into float then: ",number_float)