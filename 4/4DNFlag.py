"""Problem 4: Dutch National Flag Problem
Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, 
sort the array in a single traversal. 
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.
"""

def sort_012(input_list): # TC of O(n) where n is number of elements in the array
    #maintain 3 pointers in an array containing 3 distinct elems
    #comparing each elem to the pointers and swapping accordingly in order to avoid multiple traversals
    low = 0 # point at the first elem
    high = len(input_list) - 1 # point at the upper edge of the array
    indx = 0 # keep track of the current elem when traversing
    while indx <= high:
        if input_list[indx] == 0: #if index is 0 we can assume the low index can be wither 0 or 1 therefore assign the indx position and value to the low pointer
            input_list[indx], input_list[low] = input_list[low], input_list[indx] 
            indx += 1 # increment the indx pointer to traverse forwar
            low += 1 # increment the low pointer too to traverse forward
        elif input_list[indx] == 1:
            indx += 1 #inrcement only the indx pointr to facilitate traversal
        else:
            input_list[indx], input_list[high] = input_list[high], input_list[indx]
            high -= 1

    
    return input_list



def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
test_function([1])
test_function([1, 1,  1, 1])



"""
refernces:
https://www.educative.io/answers/the-dutch-national-flag-problem-in-cpp
https://en.wikipedia.org/wiki/Sorting_algorithm
https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
https://medium.com/quick-code/dutch-flag-algorithm-3669af2b14fd#:~:text=Dutch%20Flag%20Algorithm%20(DFA)%20is,algorithm%20is%20O(1).
https://levelup.gitconnected.com/the-dutch-national-flag-problem-be2e1e3a58a9


"""
