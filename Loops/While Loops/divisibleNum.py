num = 0 
while num <= 20:   # check condition
    num += 1       # increment num by 1
    if num % 3 == 0:
        continue
    print("this number %i is divisible by 3" %(num))  # return all numbers NOT divisible by 3: