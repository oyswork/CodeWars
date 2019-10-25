""" Given two arrays a and b write a function comp(a, b) that checks whether the two arrays have the "same" elements 
with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order. """

def comp(array1, array2):
    answer = []
    print(array1, array2)
    if array1 != None and array2 != None:
        if len(array1) == len(array2) and len(array1) > 0:
            for index,item in enumerate(sorted(array1)):
                if item**2 == sorted(array2)[index]: 
                    answer.append('same')
                else:
                    answer.append('different')
                    
            if set(answer) == {'same'}:
                print('True')
                return True
                
            else:
                print('False')
                return False
        elif len(array1) == len(array2) and len(array1) == 0:
            print('True')
            return True
        else:
            print('False')
            return False
    else:
        print('False')
        return False

""" YOU FUCKING IDIOT, HERE IS HOW ITS DONE:
def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False """
