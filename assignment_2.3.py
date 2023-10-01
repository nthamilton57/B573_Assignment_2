#here we will define a function to generete a certain length list of fibonacci numbers
def fib_nums():
    #The number of numbers generated is determined by user input.
    num = input("Enter an integer!   ")
    #if the number is 0, the program will ask the user to reenter a positive number.
    if int(num) == 0:
        num = input("Please enter a positive integer.   ")
        
    #if the number is 1, the list will just be the first fibonacci number, 1.
    if int(num) == 1:
        fib_seq = [1]
        return fib_seq
        
    #if the number is greater than 1, numbers will be appended to the list
    if int(num) > 1:
        #two numbers that will be used to append are initialized as 1
        num1, num2 = 1,1
        #the empty list is created
        fib_seq = []
        #our counter is set to 0
        n = 0
        
        #while the counter is less than the number of fibonacci numbers we want, we will append another number
        while n < int(num):
            #we will always start the cycle with appending num1
            fib_seq.append(num1)
            #update is a variable used to update num2 and num1
            update = num1 + num2
            #num 1 is set to num 2
            num1 = num2
            #num2 is set to update since a fibonacci number is defined as the number you get when adding the previous two
            num2 = update
            #our counter is increased by 1
            n += 1
            
        #return the sequence
        return fib_seq

#define a function that will generate a list of the quotients of the fibonacci number list defined previously
def fib_quot(alist):
    #initialize the list that is just 1
    fib_quot = [1]
    #set our counter equal to 0
    n = 0
    #if the len of the fibonacci sequence list is 1, then the quotient list will just be 1 as well
    if len(alist) == 1:
        return fib_quot
    #otherwise, we will append a values
    else:
        #while our counter is less then the list length minus 1 (to account for the fact that we will be dividing the next number in the sequence by the previous)
        while n < len(alist)-1:
            #append the quotient of the next num in the sequence by the number corresponding to the counter
            fib_quot.append(alist[n+1]/alist[n])
            #update our counter
            n += 1
    return fib_quot

#Use your second list of numbers to make a third group of numbers, where the first two elements are 0, and each subsequent element is the difference of the corresponding element in the second list and the previous element in the list group.

#create a function to create a list of differences
def fib_dif(alist):
    #initialize an empty list
    fib_dif = []
    #set the counter equal to 0
    n=0
    #while the counter is less than the len of our chosen list, we will append values
    while n < len(alist):
        #if the counter is less than or equal to 1, we will append 0s and update our counter
        if n <=1:
            fib_dif.append(0)
            n += 1
        #otherwise, we will append the number in the list minus the previous number in the list and update our counter
        else:
            fib_dif.append(alist[n]-alist[n-1])
            n += 1
    #return the sequence
    return fib_dif

#create a variable for the initial fib_nums function
fib_seq = fib_nums()

#use the output from the fib_nums function as the input for the fib_quot function
fib_quot_list = fib_quot(fib_seq)

#use the output from the fib_quot function as the input for the fib_dif function
fib_dif_list = fib_dif(fib_quot_list)

#print each list
print(fib_seq)
print(fib_quot_list)
print(fib_dif_list)
