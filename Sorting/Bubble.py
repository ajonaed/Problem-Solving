def bubbleSort(nums):
    length = len(nums)
    for i in range(0,length):
        # pick the first two element and compare, the bigger one will go to right
        # if both are in order, move the pointer to next two. not from start.
        for j in range(0,length-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
def main():
    nums  = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    print(bubbleSort(nums))

if __name__ == '__main__':
    main()
