""" The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray. """

def maxSequence(arr):
    best_start = best_end = 0
    current_start = current_end = 0
    best_sum = current_sum = 0
    for current_end,number in enumerate(arr):
        if current_sum <= 0:
            current_start = current_end
            current_sum = number
        else:
            current_sum += number
        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1
    print(best_sum,arr[best_start:best_end])
    return best_sum

""" you idiot, good solution is right here:
def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    print(max)
    return max """

maxSequence([-2, -1, -3, -4, -1, -2, -1, -5, -4])