def longest(s1, s2):
    return ''.join(sorted(set([letter for letter in s1] + [letter for letter in s2])))
#idiot, you can concatinate strigns, why do you need lists? ''.join(sorted(set(s1+s2))) THATS IT!