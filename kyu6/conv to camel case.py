teststr = 'abc-def-ghk'
karl = teststr.translate(teststr.maketrans('-_', '  ')).split()
karl = ''.join([item.capitalize() if index > 0 else item for index,item in enumerate(karl)])
print(karl)


# def DNAtoRNA(dna):
#     return dna.replace('T', 'U')
