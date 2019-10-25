arr = [1,100,50,-51,1,1]
def find_even_index(arr):
    for index,item in enumerate(arr):
        # print(f' Sum before element: {sum(arr[:index])}\nSum after element: {sum(arr[index+1:])}\n Index: {index}\n Element: {item}\n')
        if sum(arr[:index]) == sum(arr[index+1:]):
            print(index)
            return index
    else:
        print('-1')
        return -1


find_even_index(arr)
