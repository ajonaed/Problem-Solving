
''' Linear Search takes O(n) time, we iterate through each item of the List
    and compare if that is the desire item.
'''
def findBYLS(nums, n):
    for i in range(0,len(nums)):
        if nums[i] == n:
            return i
    return 'Not in the List!'
def main():
    nums  = [99, 44, 6, 2, 1, 5, 63, 0, 87, 283, 4, 555]
    #print(nums.index(9)) if value not on the list, ValueError will be the output
    print(findBYLS(nums,9))

if __name__ == '__main__':
    main()
