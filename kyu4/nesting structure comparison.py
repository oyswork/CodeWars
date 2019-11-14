def same_structure_as(original, other):
    print(original, other)
    if type(original) == type(other):
        original_structure = [[str(type(element)), len(
            str(element))] for element in original]
        other_structure = [[str(type(element)), len(str(element))]
                           for element in other]
        if original_structure == other_structure[::-1] and True not in [isinstance(element, list) for element in original]:
            print(original_structure == other_structure[::-1])
            return original_structure == other_structure[::-1]
        else:
            print(original_structure == other_structure)
            return original_structure == other_structure
    else:
        print('False')
        return False


same_structure_as([1, '[', ']'], ['[', ']', 1])


# https://www.codewars.com/kata/nesting-structure-comparison/train/python
