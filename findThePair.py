''' When given list is sorted, we can have two pointers, one from beginning, another at the end.
    we add bothe poiters value and check wheter it is equal to target value, we will have Linear or O(n).
    If the list is not sorted, then we can use set, difference of target value and current index value
    will be stored in the set to store the complement value and check whether we saw the complement before.
'''

def findThePairInSortedList(list_1,target):
    startPoint = 0
    endPoint   = len(list_1)-1

    while startPoint < endPoint :
        sum = list_1[startPoint] + list_1[endPoint]
        if sum == target:
            return [list_1[startPoint],list_1[endPoint]]
        elif sum < target:
            startPoint += 1
        else:
          endPoint -= 1
    return [0,0]

def findThePairInUnSortedList(list_1,target):

    comp = set()  # For storing complement

    for item in list_1:
        complement = target - item
        if complement in comp:  # did I see the complement before,
            return [item , complement]
        else:                   # if  I didn't see the complement, store it to the set.
            comp.add(complement)
    return [0,0]                # Once done iterating the list, return [0,0] as no pair available.


def main():
    list_1 = [1,2,5,9]
    list_2 = [1,2,4,4]
    print('Sorted List: ',findThePairInSortedList(list_1,10))
    print('Sorted List: ',findThePairInSortedList(list_2, 10))

    list_1 = [1,5,11,9]
    list_2 = [1,4,2,4]
    print('Unsorted List: ',findThePairInUnSortedList(list_1,8))
    print('Unsorted List: ',findThePairInUnSortedList(list_2,8))

if __name__ == '__main__':
    main()
