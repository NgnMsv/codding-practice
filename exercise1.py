def main():
    numbers = []
    for i in range(10):
        num = int(input())
        numbers.append(num)
    primelist = primes(max(numbers))
    finalArr = []
    mainEl = 0
    maxLen = 0
    for n in numbers:
        tempArr = []
        sum = 0
        for p in primelist:
            if n%p == 0:
                tempArr.append(p)
                sum += 1
        #print(n , sum , tempArr)
        if sum >= maxLen:
            if n > mainEl:
                maxlen = sum
                mainEl = n
        print(maxlen , mainEl)
    #print(mainEl, maxlen)
    
    finalArr

def primes(max):
    primeList = []
    for i in range(2 , max):
        isprime = True
        for j in range(2 , i):
            if (i%j) == 0:
                isprime = False 
        if isprime == True:
            primeList.append(i)
    return primeList
if __name__=="__main__":
    main()