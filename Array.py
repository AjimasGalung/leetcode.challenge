# Challenge Name : Binary Search
# Here, we are given with array of integers, named nums which is sorted in ascending order, and an integer named target.
# We are asked to write a function to search target in nums. If target exists, then return its index. Otherwise, return -1
# The algorithm must be O(logn) runtime complexity.

def search(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            return mid
        return -1
