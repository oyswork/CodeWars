# def balanced_parens(n):
#     table = [['']]
#     for j in range(1, n + 1):
#         result = []
#         for i in range(j):
#             for x in table[i]:
#                 for y in table[j - i - 1]:
#                     result.append('(' + x + ')' + y)
#         table.append(result)
#     return table[n]

print(balanced_parens(5))

def balanced_parens(n):
    pass    
#not finished
