number = input("Enter a number: ")

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

#2
num1 = input("enter your first number")
num2 = input("enter your second number")
num3 = input("enter your third number")

large = num1
if num2 > large:
    large =num2
if num3 > large:
    large = num3

print("The largest number is:", large)

small = num1
if num2 < small:
    small=num2
if num3 < small:
    small = num3

print("The smalles number is:", small)

if num1 == num2 == num3:
    print("All numbers are equal.")
#3
year = int(input("enter a year:"))

if year % 4 == 0 and year % 100 != 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
