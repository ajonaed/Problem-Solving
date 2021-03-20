def insertionSort(nums):
    length = len(nums)
    for i in range(1,length):
        min = nums[i]
        j = i-1
        while j >= 0 and min < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = min

    return nums

def main():
    nums  = [99, 44, 6, 2, 1, 5, 63, 0, 87, 283, 4, 0]
    print(insertionSort(nums))

if __name__ == '__main__':
    main()
