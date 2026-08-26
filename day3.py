# Conditionals
##Conditional statements - allow to run certain lines of code, depending on whether certain conditions are met
# using if elseif
#conditional states aka control structures or decision structures

weather = "cold"

if weather == "cold":               #use the colon to start the code block
    print("wear a jacket")

#################
# elif <-executes if all previous conditions failed
# else <- the else keyword is not followed by a condition, only a code block, if it reached this else, it means all else have evaluated to false

x = 5

if x < 2:
    print("small")
elif x < 10:
    print("medium")
else:
    print("large")

#nested conditions - conditions statements inside condition statements

if x > 1:
    print("more than one")  #can become dificult to read and are better when avoided
    if x < 100:
        print("less than 100")
print("all done")

#### the code snipet above can be re-written uing logical operator 
## by checking that both sttements are true instead of one by one

if x > 1 and x < 100:
    print("more than one")
    print("less han 100")
print("all done")


#for -- loops are definite iteration. You use them when you know in advance—or can easily
#measure—how many items or iterations you are dealing with (like repeating 10 times or
#looping through a list of 5 items).

#while -- loops are indefinite iteration. You use them when the loop depends on a
#dynamic condition rather than a count, meaning it will run continuously until a specific
#condition changes (like waiting for user input or waiting for a game-over flag).
## (WHILE a condition is met, do this task)

#normally a while will be used with a Iteration Variable
# the iteration variable is a variable that is set to change in value everytime a loop is repeated once; in this case n = 5 and will chnage

n = 5
while n > 0:
    print(n)
    n = n - 1
print("blastoff!")
print(n)

#output: 5,4,3,2,1,blastoff!,0

## break statement -- Terminates loop entirely when encountered
#in the example below: itll ask for someones name until they enter a name, if nothing is typed itll keep on asking over again

while True:
    name = input("enter your name")
    if name != "":          #if name doesnt equal a set of quotes(if they dont type anything)
        break

## continue - skips to the next iteration of the loop
#in the example below, want to display a number without the dahses - 

phone_num = "808-123-321"

for i in phone_num:
    if i == "-":        #if i is equal to a dash 
        continue        # then it skips that ieration of the loop
    print(i)


### input() - funtion is a built in function that instructs python to pause and read data from user
## data passed in will always be a strinng; even if a num int is enttered, itll be a string data type
##  variable = input(promt asked)
# the code will prompt user to enter their name then store the var in the varibale callled name
nombre = input("what is your name?")

print(nombre)   #itll print name enterred
