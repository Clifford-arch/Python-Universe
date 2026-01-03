def largest_num(array):
    high=array[0]
    for num in array:
        if high < num:
            high=num
    return high

print(largest_num([4,5,6]))