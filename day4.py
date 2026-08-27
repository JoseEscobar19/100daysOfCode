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
