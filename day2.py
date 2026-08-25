# Math operators
#+,=,/,*,//,**,%
# // <- this is to get no float data type when doing division


# Comparison Operators ; evaluate boolean expressions to either True or False
# for example is x greater than or equal to y; result if thats true and false if not
# >, <, >=, <=, ==, !=
# == <- this is equal to operator
# =   <- this is assignment operator


# Logical operators used to compare multiple values or values
#expressions formed from logial operators are also bollean - they evaluate to true or false
# AND <- connects 2 expressions; both have to be true to output a true expresions
# OR  <- connects 2 expressions, only 1 has to be true to output a true expression
# NOT. <- takes 1 expression and reverses its logical value, if takes true itll reverse to false, if false reveses to true

#/////////////////////////
a = 1

b = 30.5
print(type(b))

c = "Pepe"
print(type(c))

d = a + b
print(d)

##############################

#Conditional statements - allow to run certain lines of code, depending on whether certain conditions are met
# using if elseif
#conditional states aka control structures or decision structures

weather = "cold"

if weather == "cold":               #use the colon to start the code block
    print("wear a jacket")

