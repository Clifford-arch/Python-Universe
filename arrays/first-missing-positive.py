"""Find the first/ smallest positive missing number """
def first_pos_miss(array):
    n=len(array)

    #first place the the numbers in the array as per their position
    for i in range(n):
        while 1<=array[i]<=n and array[array[i]-1]!=array[i]:
            #Swap array[i] to its correct position
            array[array[i]-1],array[i]=array[i],array[array[i]-1]

    #find first pos missing number
    for i in range(n):
        if array[i]!=i+1:
            return i+1
    
    return n+1

print(first_pos_miss([3,4,-1,1]))