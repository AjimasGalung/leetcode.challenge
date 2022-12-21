# Challenge Name : Binary Search
# Here, we are given with array of integers, named nums which is sorted in ascending order, and an integer named target.
# We are asked to write a function to search target in nums. If target exists, then return its index. Otherwise, return -1
# The algorithm must be O(logn) runtime complexity.

def search(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        # Here, I use binary search algorithm, looking for the numbers at a middle
        # and make the conditions
        mid = (start+end)//2
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            return mid
        return -1
    

# Challenge : Search Insert Position
# Explanation : Given a sorted array of distinct integers and a target value, return the index 
# if the target is found. If not, return the index where it would be if it were inserted in order.
# Algorithm :
# - First, we start making the initialization for start index and end index
def searchposition(nums, target):
    start = 0
    end = len(nums) - 1
    # Second, loop and stop looping after the condition reach
    while start <= end:
        # Calculate the middle index
        mid = (start+end)//2
        # Conditional
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    # If target is not found, return the start index 
    return start
