# """ 
# Create two functions to encode and then decode a string using the Rail Fence Cipher. 
# This cipher is used to encode a string by placing each character successively in a diagonal along a set of "rails". 
# First start off moving diagonally and down. When you reach the bottom, reverse direction and move diagonally and up until you reach the top rail. 
# Continue until you reach the end of the string. Each "rail" is then read left to right to derive the encoded string.

# For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a three rail system as follows:

# W       E       C       R       L       T       E
#   E   R   D   S   O   E   E   F   E   A   O   C  
#     A       I       V       D       E       N    
# The encoded string would be:

# WECRLTEERDSOEEFEAOCAIVDEN
# Write a function/method that takes 2 arguments, a string and the number of rails, and returns the ENCODED string.

# Write a second function/method that takes 2 arguments, an encoded string and the number of rails, and returns the DECODED string.

# For both encoding and decoding, assume number of rails >= 2 and that passing an empty string will return an empty string.

# Note that the example above excludes the punctuation and spaces just for simplicity. There are, however, tests that include punctuation. 
# Don't filter out punctuation as they are a part of the string.

# https://www.codewars.com/kata/58c5577d61aefcf3ff000081/train/python 
# """
# def up_down(lowest_value, highest_value):
#     current = lowest_value
#     delta = 1
#     while True: # Begin infinite loop
#         yield current
#         current += delta
#         if current <= lowest_value or current >= highest_value:
#             delta *= -1 # Turn around when either limit is hit

# def encode_rail_fence_cipher(string, n):
#     results = []
#     gen = up_down(1,n)
#     for num in gen:
#         results.append(num)
#         if len(results) == len(string): # your ending condition here
#             break

#     karl = list(zip(results,string))
#     test_list = []
#     for i in range(n):
#         test_list.insert(n,['0']*len(string))
#     counter = 0
#     for index,value in karl:
#         test_list[index-1][counter] = value
#         counter+=1
    
#     resulting_list = [''.join(item).replace('0','') for item in test_list]
#     print(''.join(resulting_list))


# encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE" ,3)

# def decode_rail_fence_cipher(string, n):
#     original_string = string
#     results = []
#     gen = up_down(1,n)
#     for num in gen:
#         results.append(num)
#         if len(results) == len(string): # your ending condition here
#             break

#     karl = list(zip(results,string))
#     test_list = []
#     for i in range(n):
#         test_list.insert(n,['0']*len(string))
#     counter = 0
#     for index,value in karl:
#         test_list[index-1][counter] = value
#         counter+=1
    
#     intermediate_list = [len(item) - item.count('0') for item in test_list]
#     resulting_list = []
#     for item in intermediate_list:
#         resulting_list.append(string[:item])
#         string = string[item:]

#     newstring = ''
#     gen = up_down(1,n)
#     for num in gen:
#         newstring += resulting_list[num-1][0]
#         resulting_list[num-1] = resulting_list[num-1][1:]
#         if len(newstring) == len(original_string): # your ending condition here
#             print(newstring)
#             break



# decode_rail_fence_cipher('WECRLTEERDSOEEFEAOCAIVDEN',3)


from itertools import cycle


def rail_pattern(n):
    r = list(range(n))
    return cycle(r + r[-2:0:-1])


def encode(plaintext, rails):
    p = rail_pattern(rails)
    # this relies on key being called in order, guaranteed?
    print(''.join(sorted(plaintext, key=lambda i: next(p))))


def decode(ciphertext, rails):
    p = rail_pattern(rails)
    indexes = sorted(range(len(ciphertext)), key=lambda i: next(p))
    result = [''] * len(ciphertext)
    for i, c in zip(indexes, ciphertext):
        result[i] = c
    print(''.join(result))

encode('WEAREDISCOVEREDFLEEATONCE', 3)
decode('WECRLTEERDSOEEFEAOCAIVDEN', 3)