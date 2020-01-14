def to_camel_case(text):
    cleared_list = text.translate(text.maketrans('-_', '  ')).split()
    return ''.join([item.capitalize() if index > 0 else item for index,item in enumerate(cleared_list)])

""" https://www.codewars.com/kata/517abf86da9663f1d2000003/solutions/python """

