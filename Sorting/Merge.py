def mergeSort(nums):
    #Base case to stop the
    if len(nums) == 1:
        return nums
    #find the Half
    half = len(nums) // 2
    left = nums[:half]
    right = nums[half:]
    
    mergeSort(left)
    mergeSort(right)
    # Copy data to temp list left and right
    return merge(left,right, nums)

def merge(left,right, nums):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1

        k += 1
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1
    return nums

def main():
    nums  = [99, 44, 6, 2, 1, 5, 63, 0, 87, 283, 4, 0]
    print(mergeSort(nums))

if __name__ == '__main__':
    main()
