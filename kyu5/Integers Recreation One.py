import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(int(n/i))
    for divisor in large_divisors[::-1]:
        yield int(divisor)


def gen_sum(num):
    return sum(i**2 for i in divisorGenerator(num))

 

def list_squared(m, n):
    divs = {num:gen_sum(num) for num in range(m,n+1) if math.sqrt(gen_sum(num))%1==0}
    return [list(item) for item in divs.items()]

print(list_squared(1,250))