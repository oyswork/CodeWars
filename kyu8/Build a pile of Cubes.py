""" Your task is to construct a building which will be a pile of n cubes. 
The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.
You are given the total volume m of the building. 
Being given m can you find the number n of cubes you will have to build?
The parameter of the function findNb (find_nb, find-nb, findNb) will be an integer m and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n. """

def find_nb(m,n):
    total = 0
    counter = 0
    while total <= m and n-counter > 1:
        # marks = n-counter
        # karl = (marks)**3
        total += (n-counter)**3
        counter+=1
    else:
        try:
            int(total)
        except:
            print('-1')
            return -1
        else:
            print(int(total))
            return int(total)

find_nb(4183059834009, 2022)