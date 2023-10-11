import math

print (" 1. 2*2  \n 2. 2+2  \n 3. 2/2")

choice = int(input("Yout choice"))

number = int(input("Write first  number"))
number2 = int(input("Write second number"))
if choice == 1:
	print (number * number2)
elif choice == 2:
	print (number + number2)
elif choice == 3:
	print (number / number2)
