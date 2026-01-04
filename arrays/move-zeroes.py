"""Move zeroes to the end of the array"""
def move_zeroes(array):
    # n= len(array)-1
    # for i in range(n):
    #     if array[i]==0:
    #         array[i],array[i+1]=array[i+1],array[i]
    
    # return array

    """Two pointer solution"""

    last_non_zero=0
    for i in range(len(array)):
        if array[i]!=0:
            array[last_non_zero],array[i]=array[i],array[last_non_zero]
            last_non_zero+=1
    return array

print(move_zeroes([0,1,2,6,0]))

