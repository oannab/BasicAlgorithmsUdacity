"""Problem 3: Rearrange Array Digits
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that 
their sum is maximum. Return these two numbers. You can assume 
that all array elements are in the range [0, 9]. 
The number of digits in both the numbers cannot differ by more than 1. 
You're not allowed to use any sorting function that Python provides 
and the expected time complexity is O(nlog(n)).
"""

def rearrange_digits(input_list): # Time complexity of O(n log n) where n is the number of elements and log n is the number of levels it has to traverse with each split in half of the division
# recursively divide into subarrays until each subarray has size 1
    if not input_list or len(input_list) == 0: # edge case
        return -1 
    if len(input_list) <= 1:
        return input_list
    
    mid = len(input_list) // 2  # mid index
    left = rearrange_digits(input_list[:mid]) #recursively sort in descending order
    right = rearrange_digits(input_list[mid:]) 

    return merge(left, right)


def merge(left, right): # Time complexity of O(n) where n is the number of elements in the merged list
    # Space complexity of O(n) where n is the number of elements in the merged list
    
    if not left or not right: # edge cases
        return []
        
    merged = [] # new array that holds the 2 merged sublists with space complexity of O(n) where n is the size of one dimensional array
    left_i, right_i = 0,0 
    
    while left_i < len(left) and right_i < len(right): # if sorted in descending order - TC O(n) where n is the no of elem in the list
        # if left is larger than right, append left to merged and increment left_            # else append right to merged and increment right_i
        if left[left_i] >= right[right_i]: # if left is larger than right, append left to merged and increment left_i
            merged.append(left[left_i]) # append left to merged
            left_i += 1 # increment left_i
        else:
            merged.append(right[right_i]) # append right to merged 
            right_i += 1 # increment right_i

    merged += left[left_i:] # append left to merge
    merged += right[right_i:] # append right to merge
 #
    #sorted_list = merge(left, right)
    return merged
    

def test_function(test_case): # Time complexity of O(n log n), n is the no of elems in the list
    # Space Complexity of O(n) where n is the no of elems in the list due to merge/sort implementation
    
    output = rearrange_digits(test_case[0]) # TC is O(n log n) as it creates recursion over each layer of the subarray traversed
    solution = test_case[1] # solution is the 2nd element in the test case

    num1 = 0 # new str that repreesents the first number - even indexed elements
    num2 = 0 # ssecond new str that indicates the second number - odd indexed elements
    if output == -1:
        print ("Empty array")
    else:
        for i, num in enumerate(output): # Time complexity of O(n) where n is the number of elements in the list for the loop to iterate through the entire length of the list.
            if i % 2 == 0: # TC - O(n) - if i is an even number, append nums[i] to num1 
                num1 = num1 * 10 + num # multiple of 10 of fisrt num and add the current number to it
            else:
                num2 = num2 * 10 + num
            # if i is an odd number, append nums[i] to num2 
            # Time complexity of O(n)


    print('output', output)
    solution = test_case[1]
    print('solution',  solution) 

    if [num1, num2] == solution:  # Compare num1 and num2
        print("Pass")
    else:
        print("Fail")



print("Test 1: ")
test_function([[1, 2, 3, 4, 5], [542, 31]])
print("Test 2: ")
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
print("Test 3: ")
test_function([[8], [8]])
print("Test 4: ")
test_function([[], []])
print("Test 5: ")
test_function([[7, 7, 8, 8, 9, 9], [987, 987]])
"""
References:
https://www.youtube.com/watch?v=qEIGhVtZ-sg
https://stackoverflow.com/questions/55193968/minimum-and-maximum-sums-from-a-list-python
https://github.com/viralj/nd256_project3/blob/master/solution_3.py
https://realpython.com/python-min-and-max/
https://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form/
https://gist.github.com/JeffOgah/3c8e88e789c9fd45b26510eed6edac29
https://stackoverflow.com/questions/31164749/algorithm-complexity-if-else-under-for-loop
"""