""" Given an array of positive or negative integers

I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

Example:

I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes:

It can happen that a sum is 0 if some numbers are negative!
Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.

In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings. """
import math as m
def sum_for_list(lst):
    primes = [x for x in range(2, max([abs(item) for item in lst])+1) if all(x % y != 0 for y in range(2, int(m.sqrt(x)) + 1))]
    result = [(prime, sum([item for item in lst if item%prime == 0])) for prime in primes for item in lst if item%prime==0]
    result = sorted(set(result))
    result = [list(item) for item in result]
    print(result)
    #print([item for index,item in enumerate(sorted(result)) if list(sorted(result))[index] != list(sorted(result))[index-1]])

sum_for_list([50, -127, -198, -59, -26, 29, -62, -147, -164, -78, 78, -147, -168])