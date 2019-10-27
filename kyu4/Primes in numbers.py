import math
import timeit

def primeFactors(n):
    primes = (num for num in range(2,int(math.sqrt(n)+1)) if all(num%karl != 0 for karl in range(2,num)))
    count = 0
    result = ''
    for i in primes:
        while n > 1:
            if n%i==0:
                n = int(n/i)
                count += 1
            else:   
                if count > 1:
                    result += f'({i}**{count})'
                    count = 0
                    break
                elif count == 1:
                    result += f'({i})'
                    count = 0
                else:
                    break
        else:
            result += f'({i}**{count})'
            break
    else:
        result += f'({n})'
    #karl = result.replace('**1','')
    print(result)

primeFactors(933555431)