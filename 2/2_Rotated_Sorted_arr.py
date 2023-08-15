"""Problem 2: Search in a Rotated Sorted Array
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.
Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
You are given a target value to search. If found in the array return its index, otherwise return -1.
You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).
Example:
Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
Here is some boilerplate code and test cases to start with:"""
"""  use a modified binary search algorithm and then perform binary search un the subarray"""

def rotated_array_search(input_list, number): # O(log n) where n is the length of the input array
    # the function recursively searches the array and each recursion reduces the search space in half
    # Space complexity is constant - O(1) - used for variables
  
    if not input_list: # check if the input array is empty
        return -1
    if len(input_list) == 1: # check if the input array has only one element
        if input_list[0] == number:
            return 0
        else:
            return -1
    
    low = 0 # first element in array - pointer
    high = len(input_list) - 1 # end of array - pointer

    while low <= high: # O(log n) - binary search
        mid = (low + high) // 2 # mid pointer
        
        if input_list[mid] == number:
            return mid
        if input_list[low] <= input_list[mid]: # check if left half is sorted in non-decreasing order
            if input_list[low] <= number and number < input_list[mid]: # check if number is in left half  
                high = mid - 1 # update the high pointer to correspond to the mid so we can halve the search space in the lower half
            else:
                low = mid + 1 # update the low pointer to correspond to the mid so we can halve the search space in the upper half

        else: # check if right half is sorted in non-decreasing order
            if input_list[mid] < number and number <= input_list[high]: # check if number is in right half
                low = mid + 1 # update the low pointer to correspond to the mid so we can halve the search space in the upper half
            else:
                high = mid - 1 # update the high pointer to correspond to the mid so we can halve the search space in the lower half    

    return -1 # if the number is not found in the array


def linear_search(input_list, number): # Time complexity - linear search - O(n), is the length of list
    # SPace complexity O(1) - constant space used to store variables only
    for index, element in enumerate(input_list): # O(n), for loop + traverse the list with enumerate() which returns an object which can be iterated -> returns a tuple containing a count  
        if element == number: # check if the element is equal to the number given by the user 
            return index # return the index of the element in the list
    return -1
    
def test_function(test_case): # Time - O(n), n is the length of the input list given by the linear_search() + rottaed_array_search
    input_list = test_case[0]
    number = test_case[1]

    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        if linear_search(input_list, number) == -1:
            print("Number not found") # the number was correctly not found in the array
        else:
            print("Pass")    
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 100])

test_function([[], 1]) # empty array test case
test_function([[1], 1]) # single element array test case

large_array = [i for i in range(1, 1000001)] # create a large array

test_function([large_array, 4000]) # test case for large array
test_function([large_array, -1343]) # test case for element not in large array
