# Find the target element in the sorted array

#Time Complexity O(N)
#Space Complexity O(1)
def BruteforceSearch(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

#Time Complexity O(log N)
#Space Complexity O(1)
def BinarySearch(nums, target):
    high = len(nums) - 1
    low = 0

    while low <= high:
        mid = high + low // 2 # low + (high-low) // 2) Don't overflow

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1