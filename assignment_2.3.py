def fib_nums():
    num = input("Enter an integer!   ")
    if int(num) == 0:
        num = input("Please enter a positive integer.   ")
        
    if int(num) == 1:
        fib_seq = [1]
        #print(fib_seq)
        return fib_seq
        
    if int(num) > 1:
        num1, num2 = 1,1
        fib_seq = []
        n = 0
        
        while n < int(num):
            fib_seq.append(num1)
            update = num1 + num2
            num1 = num2
            num2 = update
            n += 1
            
        #print(fib_seq)
        return fib_seq

def fib_quot(list):
    fib_quot = [1]
    n = 0
    if len(list) == 1:
        return fib_quot
    else:
        while n < len(list)-1:
            fib_quot.append(list[n+1]/list[n])
            n += 1
    return fib_quot

#Use your second list of numbers to make a third group of numbers, where the first two elements are 0, and each subsequent element is the difference of the corresponding element in the second list and the previous element in the list group.

def fib_dif(list):
    fib_dif = []
    n=0
    while n < len(list):
        if n <=1:
            fib_dif.append(0)
            n += 1
        else:
            fib_dif.append(list[n]-list[n-1])
            n += 1
    return fib_dif

fib_seq = fib_nums()
fib_quot_list = fib_quot(fib_seq)
fib_dif_list = fib_dif(fib_quot_list)

print(fib_seq)
print(fib_quot_list)
print(fib_dif_list)