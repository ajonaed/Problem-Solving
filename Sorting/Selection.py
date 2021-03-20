def selectionSort(nums):
    length = len(nums)
    for i in range(0,length):
        min = i
        for j in range(i+1,length):
            if nums[j] < nums[min]:
                min = j
        nums[i],nums[min] = nums[min] ,nums[i]

    return nums
def main():
    nums  = [99, 44, 6, 2, 1, 5, 63, 0, 87, 283, 4, 0]
    print(selectionSort(nums))

if __name__ == '__main__':
    main()
