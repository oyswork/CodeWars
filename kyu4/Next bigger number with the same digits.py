""" You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

12 ==> 21
513 ==> 531
2017 ==> 2071
If no bigger number can be composed using those digits, return -1:

9 ==> -1
111 ==> -1
531 ==> -1 """

# def next_bigger(n):
#     if sorted([int(element) for element in str(n)])[::-1] != [int(element) for element in str(n)]: 
#         karl = n+1
#         while sorted([int(element) for element in str(karl)]) != sorted([int(element) for element in str(n)]):
#             karl += 1
#         return karl
#     else: return -1

def next_bigger(n):
    digits = [int(d) for d in str(n)]
    leading_zeros_passed = False
    minDigitPosition = None
    i = len(digits)
    while i > 1:
        i = i - 1
        digit = digits[i]
        nextDigit = digits[i-1]
        if digit == 0 and not leading_zeros_passed:
            continue
        leading_zeros_passed = True
        if minDigitPosition is None or digit < digits[minDigitPosition]:
            minDigitPosition = i
        if nextDigit < digit:
            digits[i-1]=digits[minDigitPosition]
            digits[minDigitPosition]=nextDigit
            return int(''.join(map(str, digits)))

    return -1
    
    print(karl)


next_bigger(531)

""" bruteforce approach, think of a better solution.
https://www.codewars.com/kata/55983863da40caa2c900004e/solutions/python """