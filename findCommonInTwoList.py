# Given 2 list of integer, create a function to find the common item in both list
#return the pair,

def findCommonItem(list_1,list_2):

    '''My Thought: the brute force is to O(n^2), the process is for each element, iterate all element of the second list,
    if we have a common element, push that into the list,Worst case = O(n^2), average case = O(n * m) m is the second list's input size.
    we  an have liner or O(2n), by using a set below is implementation '''
    result = []
    item_keeper = set()

    if len(list_1) <= len(list_2):
        for item in list_1:
            item_keeper.add(item)
    else:
        for item in list_2:
            item_keeper.add(item)

    for item in list_1:
        item_keeper.add(item)
    for item in list_2:
        if item in item_keeper:
            result.append(item)

    return result



def main():
    list_1 = [2,4,5,6,1000,1221,1221,211,1151,111444]
    list_2 = [1,3,7,9]

    list_3 = [8,11,15,19]
    list_4 = [8,11,17,20,12,111111,22222,3333,4444,5555,6666,3333,4444,78451]
    print(findCommonItem(list_1,list_2))
    print(findCommonItem(list_3,list_4))



if __name__ == '__main__':
    main()
# def common_member(a, b):
#     a_set = set(a)
#     b_set = set(b)
#
#     # check length
#     if len(a_set.intersection(b_set)) > 0:
#         return(a_set.intersection(b_set))
#     else:
#         return("no common elements")
#
#
# a = [1, 2, 3, 4, 5]
# b = [5, 6, 7, 8, 9]
# print(common_member(a, b))
#
# a =[1, 2, 3, 4, 5]
# b =[6, 7, 8, 9]
# print(common_member(a, b))
# def common_member(a, b):
#    return [element for element in a if element in b]
#
#
# a = [1, 2, 3, 4, 5]
# b = [5, 6, 7, 8, 9]
# print(common_member(a, b))
#
# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9]
# print(common_member(a, b))
