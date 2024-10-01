'''def multiply(num1, num2):
    print(num1)
    if num1 == 1:
        return num2
    return num2 * multiply(num1-1, num2)

multiply(2, 3)'''


def binary_search(search_list, search_num, low, high):
    mid = int(low+high/2)
    if search_list[mid] == search_num:
        print(f'Number Found')
        return mid
    elif search_list[mid] < search_num:
        return binary_search(search_list, search_num, low, mid-1)
    elif search_list[mid] < search_num:
        return binary_search(search_list, search_num, mid+1, high)


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binary_search(num_list, 1, 0, len(num_list))
