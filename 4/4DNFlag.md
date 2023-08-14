**Requirement**
* Problem 4: Dutch National Flag Problem
- Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. 
- You're not allowed to use any sorting function that Python provides.

 - Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.
* 

**sort_012()**
- Time complexity is O(n), where n is the length of input data
- Traverse the input array with a while loop with 3 pointers that perform constant-time O(n) operations like comparisons and swaps
- Number of iterations for the loop depend on n of 0's, 1's and 2's 
- The sorting is in linear time without using additional space

- Space Complexity is given by the variables used in sort_012() which are the 3 pointers in this case and the input array as an argument. 
- The pointer variables are O(1) as they do not scale and only use constant temporary memory. 
- The input_list argument variable does not scale or use other external inputs or data structures, therefore the space complexity remains constant O(1)