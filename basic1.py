# data tybe , if statement ,


# ----------- int -----------

x = 10
x2=-7988934584684
x3 = 0

# ----------- flout -----------

y = 0.0
y2 = float(x)
y3 = -85.3

# ----------- complex -----------

c = 8 + 2j
c1 = 9j
c2 = complex(8,2)

# ----------- coment -----------

# i'm a singel coment
""" i'm a coment """

# ----------- variable name = value -----------

x = 3
y = 9.8
t = "ok"

# ----------- variable rules -----------
 
number = 5
_number = 7
#@number = 6          (error)
# number = 5          (error)
#$number = 5          (error)
#4number = 5          (error)

studant_name = "Ahmad"
Studant_Name = "Eslam"
#studant name = "Ahmad"        (error)

studantName = "Eslam"
StudantName = "Ahmad"

# ----------- boolean -----------

t = True
f = False

t1 = bool(1)
f1 = bool(0)
t2 = bool (2)   # from 2-- to infinete

# ----------- print ----------- 

num1 = 10
num2 = 5

str1 = "python"
str2 = "10"

#print(num1)
#print(num2)

#print(num1,num2)
#print ("\n")   # or print()
#print(num1,"\n",num2,"\n")
#print(str1,str2)

"""
        # propetis : end="" : place a break between place two printing lines 
print(num1,num2,end=" ")
print(str1,str2)

        # propetis : sep="" : to place a separator between variables
print(num1,num2,str1,str2,sep="_")

"""

# ex :  Eslam_2003*python+10

name = "Eslam"
Id = 2003
course = "python"
sec = 10

"""
print(name,Id,sep="_",end="*")
print(course,sec,sep="+")
"""


# ----------- Arithmetic operators ----------- 

"""
operators      name

+              Addition
-              Subtraction
*              Multiplication
/              Division
%              Modulus
**             Exponentiation
//             Floor division
"""
"""
x = 5
y = 10
g = 3.5878
b = 7.5
z = x + y

add = x+g
d =g+b
sub = x-g
mul = x*y
div = g/y
mod = 55%10
exp = y**2  #y^2
"""

# ----------- Comparison operators ----------- 

""" 
operators       name

==              Equal to
!=              Not equal to
<               Less than
<=              Less than or equal to
>               Greater than
>=              Greater than or equal to

"""

# ----------- Comparison operators ----------- 

"""
A       B       A OR B          A       B       A AND B         A       NOT A
TRUE    TRUE    TRUE            TRUE    TRUE    TRUE            TRUE    FALSE
TRUE    FALSE   TRUE            TRUE    FALSE   FALSE           FALSE   TRUE
FALSE   TRUE    TRUE            FALSE   TRUE    FALSE
FALSE   FALSE   FALSE           FALSE   FALSE   FALSE

"""

# -----------  input ----------- 

"""
#print("enter first number :")
#num1 = int (input("enter first number : \n"))

#num1 = int (num1)

#read 2 number from the user
num1 = int (input("enter first number:\n"))
num2 = int (input("enter secound number: \n"))

#add 2 number

#res num1 + num2

print("the result is ", num1+num2)

"""

# ----------- If statement  -----------

# If (condition)
        # if () :

"""
num = int (input ("enter number to check if is odd or even : \n"))

if num % 2 == 0 :
    #print(num , "is even")
    #print(str(num) + " is even")
    print(f"{num} is even")
"""

"""
num1 = int (input ("enter first number : \n "))
op = input("enter opeartion:\n")
num2 = int (input ("enter second number: \n "))

if op == "+":
        print(f"{num1} {op} {num2} = ",num1 + num2 )

if op == "-" :
        print(f"{num1} {op} {num2} = ",num1 - num2 )

if op == "*" :
        print(f"{num1} {op} {num2} = ",num1 * num2 )

if op == "/" :
        print(f"{num1} {op} {num2} = ",num1 / num2 )
"""

"""price = 50

if price < 100:
    print("price is less than 100")
"""

"""price = 50
quantity = 5
if price*quantity < 500:
    print("price is less than 500")
    print("price = ", price)
    print("quantity = ", quantity)
"""

"""
price = 100

if price > 100:
 print("price is greater than 100")

if price == 100:
  print("price is 100")

if price < 100:
    print("price is less than 100")
"""

# Else 

"""
num = int (input ("enter number to check if is odd or even : \n"))

if num % 2 == 0 :
    print(f"{num} is even")
else :
        print(f"{num} is odd")
"""

"""
x = 3
if x == 4:
   print("Yes")
else:
   print("No")
"""

"""
etter = "A"
 
if letter == "B":
  print("letter is B")
   
else: 
     
  if letter == "C":
    print("letter is C")
     
  else:
       
    if letter == "A":
      print("letter is A")
       
    else: 
      print("letter isn't A, B and C")
"""

"""
number = 10

if number < 0:
    print('Hola')

else:
    print('oui')

print('Welcome in SDK')
"""

# Nested If

"""
gender = input("enter your gender M/F: \n")

        # m = 18 , high > 165 , 55 < weight < 70
if gender == "m":
        age = int (input ("enter your Age: \n"))
        if 18 <= age <=29 :
                high = float (input ("enter your Hight :\n"))
                if high > 165:
                        weight = float (input ("enter your weight "))
                        if 55 <= weight <= 77:
                                print("accepted ")

                        else:
                           print("Sorry, your Weight not accepted")

                else:
                   print("Sorry, your Hight not accepted ")

        else:
           print("Sorry, your Age not accepted ")

else:
   print("Sorry, not accepted ")
"""

"""
num = 10
 
if num > 5:
   print("Bigger than 5")
 
   if num <= 15:
      print("Between 5 and 15")
"""

"""
number = 5

if (number >= 0):
  
    if number == 0:
      print('sava')
    
    else:
        print('python')

else:
    print('banana')
"""

#Elif

"""
num1 = int (input ("enter first number : \n "))
op = input("enter opeartion:\n")
num2 = int (input ("enter second number: \n "))

if op == "+":
        print(f"{num1} {op} {num2} = ",num1 + num2 )

elif op == "-" :
        print(f"{num1} {op} {num2} = ",num1 - num2 )

elif op == "*" :
        print(f"{num1} {op} {num2} = ",num1 * num2 )

elif op == "/" :
        print(f"{num1} {op} {num2} = ",num1 / num2 )
else :
        print("invalid opeartion")
"""

"""
num = int(input (" enter number: \n"))

if (num% 5 ==0) and (num %3 ==0) :
        print("fizz puzz ")
elif num %5 == 0:
        print("puzz")
elif (num %3 ==0) :
        print("fizz")
else :
        print ("not divisabel by 3 or 5")
"""

"""
num1 = 5
num2 = float(7)
num3 = float(33)

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)
"""

"""
score = 55.6

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("The grade is:", grade)
"""

"""
side1 = float(5)
side2 = float(7)
side3 = float(258)

if side1 == side2 and side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
"""

"""
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
    
    if year < 1583:
        print("This year is in the Julian calendar.")
    elif year == 1582:
        print("This year straddles the change from Julian to Gregorian calendar.")
    else:
        print("This year is in the Gregorian calendar.")
else:
    print("Not a leap year")
"""

# examples

"""
Exercise 1: Number Comparison Write a program that takes two numbers as input and 
prints whether the first number is greater, smaller, or equal to the second number.

Exercise 2: Tax Calculator Write a program that calculates the income tax based on 
the user's income. If the income is less than $50,000, the tax is 10%. If the income 
is between $50,000 and $100,000, the tax is 20%. Otherwise, the tax is 30%.

Exercise 3: BMI Calculator Write a program that calculates the Body Mass Index (BMI) based 
on the user's weight and height. Print a message indicating whether the person is underweight, 
normal, overweight, or obese based on the BMI.

Exercise 4: Sorting Numbers Write a program that takes three numbers as input and prints them 
in ascending order.


x = float(input("input first number: "))
y = float(input("input second number: "))
z = float(input("input third number: "))


if(x>y):
    if x>z:
        print(f"max{x}")
        if y>z:
            print(f"mid{y}\n min{z}")
        else :
            print(f"mid{z}\n min{y}")
    else :
        print(f"max{z} \n mid{x} \n min{y}")

elif(y>x):
    if y>z:
        print(f"max{y}")
        if y>z:
            print(f"mid{x}\n min{z}")
        else :
            print(f"mid{z}\n min{x}")
    else :
        print(f"max{z} \n mid{y} \n min{x}")


        

Exercise 5: Day of the Week Write a program that takes a number (1-7) as input and prints 
the corresponding day of the week: "Sunday," "Monday," etc.

Exercise 6: Rock-Paper-Scissors Game Write a program that simulates a simple rock-paper-scissors game. 
Take the user's choice as input and determine the winner.

Exercise 7: Age Group Classifier Write a program that takes a person's age as input and classifies them 
into different age groups: "Child" (0-12), "Teen" (13-19), "Adult" (20-59), or "Senior" (60+).


age = int(input("enter age: "))

if age < 0: 
    print("invalid Age")

elif 0<= age <=12 : 
    print("Child")

elif 13<= age <=19 :
    print("Teen")

elif 20<= age <=59: 
    print("Adult")

else: 
    print("Senior")

    

Exercise 8: In this exercise you will create a program that reads a letter of the alphabet from the user. 
If the user enters a, e, i, o or u then your program should display a message indicating that 
the entered letter is a vowel. If the user enters y then your program should display 
a message indicating that sometimes y is a vowel, and sometimes y is a consonant. 
Otherwise your program should display a message indicating that the letter is a consonant

"""

