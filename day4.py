## practice conditional statement
'''
Students  |  Grades  |  Letters
------------|----------|----------
  George    |  46      |  F
  Michell   |  80      |  B
  Josh      |  12      |  F
  Chloe     |  68      |  D
  Stanley   |  99      |  A
  Annie     |  100     |  A+
  '''
#gradeTest = 11
gradeToTest = int(input("enter your grade"))
if gradeToTest == 100:
    print("A+")
elif gradeToTest >= 90:
    print("A")
elif gradeToTest >= 80:
    print("B")
elif gradeToTest >= 70:
    print("C")
elif gradeToTest >= 50:
   print("D")
else:
    print("F")
##########################

#practice nested if
priceIsRight = 15

if priceIsRight:
    print("Price is too low!")
    if priceIsRight:
        print("Price is almost there!")
        if priceIsRight:
            print("Price is exactly that!")
        if priceIsRight:
            print("Price is too high!")

#the code above is turned to code below

priceIsRight = 7

if priceIsRight < 5:
    print("Price is too low!")
elif priceIsRight >= 5 and priceIsRight <= 9:
    print("Price is almost there!")
elif priceIsRight == 10:
    print("Price is exactly that!")
else:
    print("Price is too high!")


###############################

## practice while loops

x = 0

while x != 10:
    x = x + 1
    if x < 5:
        print(x)
    elif x == 6:
        print(x)
        continue
    elif x >= 5 and x <= 8:
        print("x is bigger then or equal to 5, and less then or equal to 8, but not 6. It is:", x)
    else:
        print("x is bigger than 8. It is:", x)

#output
'''
1
2
3
4
x is bigger then or equal to 5, and less then or equal to 8, but not 6. It is: 5
6
x is bigger then or equal to 5, and less then or equal to 8, but not 6. It is: 7
x is bigger then or equal to 5, and less then or equal to 8, but not 6. It is: 8
x is bigger than 8. It is: 9
x is bigger than 8. It is: 10
'''

