import string

def is_pangram(s):
    karl = []
    s = sorted(s.split())
    for item in s:
        for symbol in item:
            karl += symbol
    karl = [symbol.lower() for symbol in karl]
    karl = list(set(karl))
    for item in karl:
        if item not in string.ascii_letters:
            karl.pop(karl.index(item))


            
    karl = ''.join(sorted(karl))
    if karl == string.ascii_lowercase:
        print(karl, 'True')
        return True
    else:
        print(karl, 'False')
        return False
""" 
you idiot. This is a good solution right here:
import string

def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())
  """   

print(is_pangram('ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ'))
