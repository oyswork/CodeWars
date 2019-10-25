def high_and_low(numbers):
    numbers = [int(num) for num in numbers.split()]
    print(numbers, max(numbers), min(numbers))
    return str(max(numbers) + ' ' + min(numbers))
    # print(result)
    # return result

high_and_low('1088 674 203 1521 -60 1636 1256 1204 2162 148 1125 -141 2890 956 521 83 919 -60 1925 67 275 330')