# while and for , 



# ----------- while and for statement -----------
#while

"""
i = 1
while i<= 10 :
    print(i)
    i += 1
   #i += 2        # even numbers
print(i)
"""

"""
i = 1
while i<= 10 :
    print(i)
    i += 2
else : 
    print(i,"out loop")
"""

"""
num=5
g_num=int(input("gess number between 1-10 \n"))

while num != g_num:
    while g_num not in range(1,11): 
        print("pleas enter number between 1-10 :") 
        g_num = int(input("gess number between 1-10 \n")) 
    print("you are wrong pleas gess anuther number : ") 
    g_num = int(input("gess number between 1-10 \n"))

else:
    print("you win the number is ",num)
"""    

# for

"""
for i in range (1,6):
    print()
    for j in range (1,6):
        print(i,"*",j,"=",i*j,end=" | ")
"""
"""
for i in range (1,15,2):
    print(i)
"""
"""
for i in range (1,15,2):
    print(i,end=" ")
"""
"""
s = "hi eslam"

for i in s : 
    print(i)
"""
"""
s = "eysylyaym"

for i in s : 
   if i == "y" :
      continue
   else :
      print(i,end="")
"""
"""
s = "eysoylyoaymo"

for i in s : 
   if (i == "y" or i == "o")  :
      continue
   else :
      print(i,end="")
"""
"""
Write a Python program to construct the following pattern using a nested for Loop

*
**
***
****
*****
****
***
**
*

n = int(input("enter number of stars , enter 0 to end \n"))
while n != 0 :
    for i in range (1,n+1):
        print(i*"*")
        if i == n :
            for j in range (i-1,0,-1):
                print(j*"*")

    n = int(input("enter number of stars , enter 0 to end \n"))            
"""   

"""
num = 9

for i in range (3,0,-1):
    user_cho = int(input("Enter number between 1-10: ")) 
    while not(1 <= user_cho <= 10) : 
        user_cho = int(input("Invalid input, please Enter numbe : "))

    if user_cho == num :
        print("winner")
        break

    else:
        print(f"try again, your chance is {i-1}")

else:
    print("Loss")
"""


# loop ex :

""""
Exercise 1: Print First 10 natural numbers using while loop.

i = 1
while i<= 10 :
    print(i)
    i += 1
__________________________________________________
Exercise 2: Print the following paƩern
Write a program to print the following number paƩern using a
loop.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
__________________________________________________
Exercise 3: Calculate the sum of all numbers from 1 to a given
number
Write a program to accept a number from a user and calculate
the sum of all numbers from 1 to a given number
For example, if the user entered 10 the output should be 55
(1+2+3+4+5+6+7+8+9+10)
___________________________________________________
Exercise 4: Write a program to print mulƟplicaƟon table of a
given numbe.
_________________________________________________
Exercise 5: Count the total number of digits in a number
Write a program to count the total number of digits in a
number using a while loop.
For example, the number is 75869, so the output should be 5.
_________________________________________________
Exercise 6: Display numbers from -10 to -1 using for loop.

for i in range (-10,0):
    print(i)
_________________________________________________
Exercise 7: Average :In this exercise you will create a program
that computes the average of a collecƟon of values entered by
the user. The user will enter 0 as a senƟnel value to indicate
that no further values will be provided. Your program should
display an appropriate error message if the first value entered
by the user is 0
"""

# ----------- Defining function -----------


"""
def function_name (parameter1, parameter2):
        statment1
        statement2
        return value to return
"""