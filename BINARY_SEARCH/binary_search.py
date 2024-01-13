import time
import random



def binary_search(my_list, target, low= 0, high = None):
    if not high :
        high = len(my_list) - 1
    

    if low > high :
        print("Not Here")
        return -1

    mid_point = (high + low) // 2

    if my_list[mid_point] == target:
        print("I Found It")
        return mid_point
    
    elif target < my_list[mid_point] :
        high = mid_point - 1
        binary_search(my_list , target, low, high )

    else:
        
        low = mid_point + 1
        binary_search(my_list, target, low, high)


if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9, 10]
    target = 4
    binary_search(my_list, target)
