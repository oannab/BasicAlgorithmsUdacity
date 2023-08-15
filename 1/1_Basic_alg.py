def sqrt(number): # Time complexity is O(log n), n is the given input, complexity is given by the binary search
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return -1
    elif number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        low = 0 # start with the lowest possible value
        high = number # end of binary search 
        while low <= high: # run until low pointer is less or equal to highher pointer
            mid = (low + high) // 2 # mid pointer
            if mid * mid == number: # check if the mid pointer is equal the number
                return mid
            elif mid * mid < number:
                low = mid + 1 # update lower pointer to search in  the upper half
            else:
                high = mid - 1 # update high pointer to search in  the upper half
        return high # floored square root
   

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

print("Pass" if  (-1 == sqrt(-1)) else "Fail") # negative input 

print("Pass" if  (0 == sqrt(0)) else "Fail") # 0 input

print("Pass" if  (1 == sqrt(1)) else "Fail") # 1 input

print("Pass" if  (2 == sqrt(5)) else "Fail") # prime number 

print("Pass" if  (3 == sqrt(9)) else "Fail") # prime number and exact square

print("Pass" if  (4 == sqrt(17)) else "Fail") # prime number and non exact square

print("Pass" if  (100 == sqrt(10002)) else "Fail") # large no and non exact square
