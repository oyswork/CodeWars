def recoverSecret(*triplets):
    triplets = list(triplets)
    flattened = ''
    karl = []
    for item in triplets:
        karl.append(item[:-1])
        karl.append(item[1:])
        for letter in item:
            flattened += letter
    flattened = list(set(flattened))
    flattened = {index:letter for index,letter in enumerate(flattened)}
    print(flattened)
    print(karl)
    print(sorted([[karl.count(item),item] for item in karl]))

recoverSecret(['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s'])