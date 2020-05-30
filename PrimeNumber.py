import sys
import math

print("Determine number is a prime number or not" + "\n")

while True:
    
    userInputNumber = input("Enter your number:")

    lastChar = userInputNumber[-1]

    #check if input number is decimal or negative
    #if yes then set lastChar to any non-prime number
    #infinite while loop is needed so that program doesn't terminate when exception
    while True:
        try:
            isPotentialPrime = int(userInputNumber)

            if isPotentialPrime < 0:
                lastChar = 4
                break
            break

        except:
            lastChar = 4
            break

    def DetermineIsPrimeNumber():
        mod = 0

        squareRoot = math.sqrt(isPotentialPrime)

        while True:

            if squareRoot == 1 or squareRoot == 0:
                print(userInputNumber + "\tis not a prime number")
                print("-----------")
                break

            #quick win if potential prime is either 2,3,5 or 7
            if isPotentialPrime == 2:
                mod = 1
            elif isPotentialPrime == 3:
                mod = 1
            elif isPotentialPrime == 5:
                mod = 1
            elif isPotentialPrime == 7:
                mod = 1

            #2,3,5,7,11,13,17,19
            #beyond that, it is repetition of above prime numbers
            #need >= 2 condition to catch 4 is not prime 
            if squareRoot >= 2:
                try:
                    assert isPotentialPrime%2 != 0
                    mod = isPotentialPrime%2
                except:
                    print(userInputNumber + "\tis not a prime number")
                    print("-----------")
                    break

            if squareRoot > 3:
                try:
                    assert isPotentialPrime%3 != 0
                    if mod == 0:
                        mod = isPotentialPrime%3
                except:
                    mod = 0
                    print(userInputNumber + "\tis not a prime number")
                    print("-----------")
                    break

            if squareRoot > 5:
                try:
                    assert isPotentialPrime%5 != 0
                    if mod == 0:
                        mod = isPotentialPrime%5
                except:
                    mod = 0
                    print(userInputNumber + "\tis not a prime number")
                    print("-----------")
                    break

            if squareRoot > 7:
                try:
                    assert isPotentialPrime%7 !=0
                    if mod == 0:
                        mod = isPotentialPrime%7
                except:
                    mod = 0
                    print(userInputNumber + "\tis not a prime number")
                    print("-----------")
                    break

            if squareRoot > 11:
                try:
                    assert isPotentialPrime%11 != 0
                    if mod == 0:
                        isPotentialPrime%11
                except:
                    mod = 0
                    print(userInputNumber + "\tis not a prime number")
                    print("-----------")
                    break

            if squareRoot > 13:
                try:
                    assert isPotentialPrime%13 != 0
                    if mod == 0:
                        isPotentialPrime%13
                except:
                    mod = 0
                    print(userInputNumber + "\tis not a prime number")
                    print("-----------")
                    break

            if squareRoot > 17:
                try:
                    assert isPotentialPrime%17 != 0
                    if mod == 0:
                        isPotentialPrime%17
                except:
                    mod = 0
                    print(userInputNumber + "\tis not a prime number")
                    print("-----------")
                    break

            if squareRoot > 19:
                try:
                    assert isPotentialPrime%19 != 0
                    if mod == 0:
                        isPotentialPrime%19
                except:
                    mod = 0
                    print(userInputNumber + "\tis not a prime number")
                    print("-----------")
                    break

            if mod != 0:
                print(userInputNumber + "\tis a prime number")
                print("-----------")
                break
    
    #determine if the input number is a potential prime
    #0,2 and 5 are not potential prime but needed to handle exception case        
    if int(lastChar) == 1:
        DetermineIsPrimeNumber()
    elif int(lastChar) == 2:
        DetermineIsPrimeNumber()
    elif int(lastChar) == 3:
        DetermineIsPrimeNumber()
    elif int(lastChar) == 5:
        DetermineIsPrimeNumber()
    elif int(lastChar) == 7:
        DetermineIsPrimeNumber()
    elif int(lastChar) == 9:
        DetermineIsPrimeNumber()
    elif int(lastChar) == 0:
        DetermineIsPrimeNumber()
    else:
        print(userInputNumber + "\tis not a prime number")
        print("-----------")
