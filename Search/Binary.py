#Non Recursive
def findBYBS(nums, n):
    high = len(nums) - 1
    low  = 0
    mid = 0
    while low <= high:
        mid = (high+low) // 2
        if nums[mid] > n:
            high = mid - 1
        elif nums[mid] < n:
            low = mid + 1
        else:
            return mid
    return 'Item is not in the list!'

#Recursive
def findByBSRecursive(nums,n):
    low = 0;
    high = len(nums) - 1
    return findNumber(nums,n,low,high)

def findNumber(nums,n,low,high):
    mid = (low+high) // 2
    if nums[mid] ==n:
        return mid
    elif nums[mid] < n:
        return findNumber(nums,n,mid+1,high)
    elif nums[mid] > n:
        return findNumber(nums,n,low,mid-1)
    else:
        return 'Number is not on the list!!1'

def main():
    nums  = [0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283, 555]
    #print(nums.index(9)) if value not on the list, ValueError will be the output
    print(findBYBS(nums,99))
    print(findByBSRecursive(nums,4))
    
if __name__ == '__main__':
    main()
