"""Move zeroes to the end of the array"""
def move_zeroes(array):
    n=len(array)-1
    for i in range(n):
        if array[i]==0:
            array[i],array[i+1]=array[i+1],array[i]
    
    return array

print(move_zeroes([0,1,2,6,0]))

