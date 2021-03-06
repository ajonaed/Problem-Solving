'''Given two sorted list,
Merge both list into one'''

def mergeSortedList(list_1, list_2):
    result = []
    i,j = 0,0
    if not list_1:
        return list_2
    if not list_2:
        return list_1
    while ( i<len(list_1) and j<len(list_2)) :
        if list_1[i] <= list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1
    if i <len(list_1):
        result.append(list_1[i])
        i += 1
    elif j < len(list_2):
        result.append(list_2[j])
        j += 1
    return result


def main():
    list_1 = [0,3,5,31]
    list_2 = [1,6,9,28]
    
    print(mergeSortedList(list_1,list_2))


if __name__ == '__main__':
    main()
