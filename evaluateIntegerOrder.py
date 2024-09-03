# This program takes inputs of three integers and
# prints "in order" for ascending or descending sort, or
# prints "not in order" if neither.

numOne = 0
numTwo = 0
numThree = 0

print("This program accepts three integers and decides ")
print("whether or not they occur in order. ")
print(" ")
# Get user input for three numbers.
numOne = int(input("Input a whole number. ")) # get first num
numTwo = int(input("Input a whole number. ")) # get second num
numThree = int(input("Input a whole number. ")) # get third num
print(" ")
# print inputs to user
print("You entered: ", numOne , " ", numTwo , " ", numThree)
print(" ")

##if numOne >= numTwo and numTwo >= numThree :
##    print("Result: in order ") # descending order
##elif numOne <= numTwo and numTwo <= numThree :
##    print("Result: in order ") # ascending order
##elif numOne > numTwo and numTwo < numThree : # neither
##    print("Result: NOT in order ")
##elif numOne < numTwo and numTwo > numThree : # neither
##    print("Result: NOT in order ")

if numOne >= numTwo and numTwo >= numOne :
    print("Result: in order ")
elif numOne <= numTwo and numTwo <= numThree :
    print("Result: in order ")
else :
    print("Result ", numOne, ",", numTwo, ",", numThree, " are not in order ")
