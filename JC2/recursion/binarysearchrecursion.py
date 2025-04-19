
def binarySearch(array, lowerbound,upperbound, num):
    if upperbound < lowerbound: #base case
        return -1
    
    mid = (lowerbound + upperbound)//2
    if num == mid:
        return mid
    if num < mid:
        return binarySearch(array, lowerbound, mid - 1, num) #recursive to lower half of array
    if num > mid:
        return binarySearch(array, mid + 1, upperbound, num) #recursive to upper half of array