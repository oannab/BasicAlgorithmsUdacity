**Problem 6: Unsorted Integer Array**
**Requirement**
- Max and Min in a Unsorted Array
- In this problem, we will look for smallest and largest integer from a list of unsorted integers. 
- The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max. 

* 

**get_min_max()**
- create min/max variables
- traverse the list by comparing the current elem with the next and IF:
    - if the current elem > than max_v, assign the current elem as the max_v
    - if the current elem < than min_v, assign the current elem as the min_v
- Therefore we only traverse the list once as we compare at each current elem -  O(1) - and assign the current values to the min/max variables if applicable - O(1)  
- Time complexity is linear - O(n), where n is the length of list to be traversed. Time complexity is given by the length of the list.
