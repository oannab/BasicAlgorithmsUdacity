**Problem 2: Search in a Rotated Sorted Array**
**requirements**
- Search in a Rotated Sorted Array
- given a sorted array which is rotated at some random pivot point.
- You are given a target value to search. If found in the array return its index, otherwise return -1.
- You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).


_Abbreviation:_
_Time Complexity = TC_
_Space Complexity = SC_


* rotated_array_search()
- binary search, halving the search space with each iteration
- TC - O(log n), due to halving the search space recursively
- SC is constant O(1), as the space for variables does not change

* linear_search()
- iterate trough the input list
- TC is O(n), n is length of the list traversed.
- SC is O(1), as the search space does not increase in size

* test_function()
- calls linear_search() + rotated_array_search()
