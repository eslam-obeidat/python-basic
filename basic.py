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