***Problem 3: Rearrange Array Digits***

**Requirements**
- Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

_Abbreviation:_
_Time Complexity = TC_
_Space Complexity = SC_

**rearrange_digits()**
- recursively divide input list into sublists
- TC is O(n log n), n is no of elems in the input list. The complexity is given by the recursion O(log n) + the merging step O(n)
- SC is O(n), n is the no of elems in the merged list. The function grows linear due to the newly sublists created with each recursive call and merged into a new lists of ssize n.

**merge()**
- merge left/right sublists in descending order. 
- TC is O(n), n is length of left + right sum. the function iterates once trough both sublists.
- SC is O(n) n is length of left + right sum. The new merged list stores the new result, which is dependant on the length of the sum of left + right subllists.

**test_function()**
- calls rearrange_digits() method into the output variables and checks if equal
- TC is O(n log n), n is the no of elems in the input list. complexity is given by the rearrange_digits() method being called within this f().
- SC is O(n), n is the no of elems in the merged list, compleixty given by the merge() method being called within the rearrange_digits(). New sublists created and merged during sorting process.
