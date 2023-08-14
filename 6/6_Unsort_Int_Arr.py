"""Problem 6: Unsorted Integer Array
Max and Min in a Unsorted Array
In this problem, we will look for smallest and 
largest integer from a list of unsorted integers. 
The code should run in O(n) time. Do not use Python's 
inbuilt functions to find min and max.
Bonus Challenge: Is it possible to find the max and min in a single traversal?
"""
def get_min_max(ints): # O(n) time and O(1) space
   """
   Return a tuple(min, max) out of list of unsorted integers.

   Args:
       ints(list): list of integers containing one or more integers
   """
   if len(ints) == 0: # edge case
      return None
   if len(ints) == 1: # edge case
      return (ints[0], ints[0]) # return both min/max vars as the first elem in the list if len(list) == 1
   if not ints:
      return None
      print("Error: Empty list")
   
   min_v = ints[0] # initialize min_v at first elem in the list
   max_v = ints[0] # set max_v at first elem in the list

   for i in ints: # traverse the whole list and check if next i is < or > than min/max variables
      if i < min_v: # compare current i with min_v 
         min_v = i # set the minimum value to current i
      if i > max_v: # compare current i with max_v to check if current i is larger then the already set max value variable
         max_v = i # set the maximum value to current i

   return (min_v, max_v) # return the min and max value              

### Example Test Case of Ten Integers
import random

## Test 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Test 1 - Pass" if ((0, 9) == get_min_max(l)) else "Fail")


## Test 2
test2 = [0,0,0,0,0,0,0,0,0,0]

print ("Test 2 - Pass" if ((0, 0) == get_min_max(test2)) else "Fail")


## Test 3
test3 = [i for i in range(-10, 10)]

print ("Test 3 - Pass" if ((-10, 9) == get_min_max(test3)) else "Fail")


## Test 4
test4 = []

print ("Test 4 - Pass" if (None == get_min_max(test4)) else "Fail")



"""Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?
"""
"""
References:
https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/
https://www.enjoyalgorithms.com/blog/find-the-minimum-and-maximum-value-in-an-array
https://sbalgobin94.medium.com/how-to-find-the-maximum-value-in-an-unsorted-array-c-30aa27219dfa
https://stackoverflow.com/questions/8374497/can-i-find-the-max-min-value-in-an-unsorted-array-in-sub-linear-time
https://sbalgobin94.medium.com/how-to-find-the-maximum-value-in-an-unsorted-array-c-30aa27219dfa

"""