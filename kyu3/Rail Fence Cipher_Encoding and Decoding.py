""" 
Create two functions to encode and then decode a string using the Rail Fence Cipher. 
This cipher is used to encode a string by placing each character successively in a diagonal along a set of "rails". 
First start off moving diagonally and down. When you reach the bottom, reverse direction and move diagonally and up until you reach the top rail. 
Continue until you reach the end of the string. Each "rail" is then read left to right to derive the encoded string.

For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a three rail system as follows:

W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C  
    A       I       V       D       E       N    
The encoded string would be:

WECRLTEERDSOEEFEAOCAIVDEN
Write a function/method that takes 2 arguments, a string and the number of rails, and returns the ENCODED string.

Write a second function/method that takes 2 arguments, an encoded string and the number of rails, and returns the DECODED string.

For both encoding and decoding, assume number of rails >= 2 and that passing an empty string will return an empty string.

Note that the example above excludes the punctuation and spaces just for simplicity. There are, however, tests that include punctuation. 
Don't filter out punctuation as they are a part of the string.

https://www.codewars.com/kata/58c5577d61aefcf3ff000081/train/python 
"""
from itertools import cycle
def encode_rail_fence_cipher(string, n):
    results = []
    i = 1
    going_forw = True
    while len(results) < len(string):
        if i < n and going_forw == True:
            results.append(i)
            i+=1
        elif i==n and going_forw == True:
            results.append(i)
            going_forw = False
        elif i==1:
            i+=1
            going_forw = True
        else:
            i -= 1
            results.append(i)
    karl = list(zip(results,string))
    test_list = []
    for i in range(n):
        test_list.insert(n,['0']*len(string))
    counter = 0
    for index,value in karl:
        test_list[index-1][counter] = value
        counter+=1
    
    resulting_list = [''.join(item).replace('0','') for item in test_list]
    print(''.join(resulting_list))
    # for item in test_list:
    #     resulting_list.append(''.join(item).replace('0',' '))
    # return '\n'.join(resulting_list)[:-1]

encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE" ,3)

#def decode_rail_fence_cipher(string, n):