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

