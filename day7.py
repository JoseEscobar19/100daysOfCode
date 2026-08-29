# For loops - used when knowing approximate num of iterations
# repeat a fixed number of times
'''Range Style ()'''
#range funtion in for loops -   this defines a fixed num of times
# for [iteration num] in range(start, end, step):
#   code of block

for i in range(0,5,1):
    print(i)

#so i is 0, once i reached to 5 itll stop, after being incremented by 1 

#################################

"""Iterable style"""
##  For loops with iterable value 
'''
 provide For loop with a iterable value like a dictionary(objects), list(array), string, sett, tuple
 this will step trhough the contents of the value such as the items inside a list or characters 
inside a string, or key value pairs in a dictionary,
once the list, dictionary,string stops the loop stops
'''

for x in "string":
    print(x)

