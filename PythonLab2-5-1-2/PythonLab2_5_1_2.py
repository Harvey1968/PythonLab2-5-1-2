#Scenario
#this program computes the number of seconds in a given number of hours
# this program has been written two days ago
a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour
print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours
#here we should also print "Goodbye", but a programmer didn't have time to write any code
print('"Goodbye"\n')
#this is the end of the program that computes the number of seconds in 3 hour
print('"Hello again!"')
b = 3
print("Hours: ", b) #printing the number of hours
print("Seconds in Hours: ", b * seconds) # printing the number of seconds in a given number of hours
print('"Goodbye"\n')

#Extra
print('"You again?"')
c = 4
print("Hours: ", c) #printing the number of hours
print("Seconds in Hours: ", c * seconds) # printing the number of seconds in a given number of hours
print('"Goodbye...?"\n')

print('"Guess not, okay fine type your own:"')
d = int(input("Enter an integer: "))
print("Answer = ", d * seconds, "seconds!", end="\n\n")
