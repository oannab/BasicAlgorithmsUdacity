**Problem 1: Calculate the floored Squared Root of a Number**
**Requirement**
- Calculate the floored square root of a number

_Abbreviation:_
_Time Complexity = TC_
_Space Complexity = SC_

 
**sqrt()**
- integer square root of non-negative no.
- binary search to find the integer sq root between low/high and calculate the mid value. for a given number, set a range intialized at [0, input_number] which is the search space.
- search for mid point and check recursively that mid is not greater than the input number whilst also halving the search space based on whether mid is less then or greater than the input no.
- the floored square root is the largest integer (mid) which is less then or equal to the input number.
- TC is O(log n), n is the input number, complexity is given by the binary search of halving the search space recursively
- SC is O(1) since the space required is constant to store variables.