#Student Name : Jaimon Thyparambil Thomas
#Student ID : 29566428

'''
Question
---------
Read a list of integers from user input.
Find all pairs of numbers in the list whose product is even and whose sum is odd.
Print out a formatted list of the pairs.
'''

def printPairsWithOddSumEvenProduct(numbers):
    evenNumbers = []
    oddNumbers = []
    # we know that inorder for a pair of numbers sum be odd and product be even
    # one of the number in the pair should be even and another should be odd
    for each in numbers:
        if (each % 2 == 0):
            evenNumbers.append(each)
        else:
            oddNumbers.append(each)
    if (len(evenNumbers) < 1 or len(oddNumbers) < 1):
        print("Sorry Out of the given numbers there is no pair such that their sum is odd and product is even")
        return
    print("Pairs with their sum being odd and product being even are:")
    for evenNumber in evenNumbers:
        res = ""
        for oddNumber in oddNumbers:
            if(len(res) != 0):
                res +=", "
            res +="("+str(evenNumber)+","+str(oddNumber)+")"
        print(res)

def bruteForcePrintPairWithOddSumEvenProduct(numbers):
    print("Pairs with their sum being odd and product being even are:")
    found = False
    for i in range(len(numbers)):
        res = ""
        for j in range(i,len(numbers)):
            product = numbers[i]*numbers[j]
            sum = numbers[i] + numbers[j]
            if(product%2 == 0 and sum %2 !=0):
                found = True
                if (len(res) != 0):
                    res += ", "
                res += "(" + str(numbers[i]) + "," + str(numbers[j]) + ")"
        print(res)
    if(not found):
        print("Sorry no such pair exist")

def main():
    numbers = []
    n = int(input("How many no do you wish to enter: "))
    while(n>0):
        n -=1
        number = int(input("Enter desired no: "))
        numbers.append(number)
    printPairsWithOddSumEvenProduct(numbers)
    #bruteForcePrintPairWithOddSumEvenProduct(numbers)
    return

if(__name__ == "__main__"):
    main()
