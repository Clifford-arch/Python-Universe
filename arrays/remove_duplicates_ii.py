def remove_duplicates_ii(array):
    if not array:
        return 0
    write=2
    for i in range(2,len(array)):
        if array[i]!=array[write-2]:
            array[write]=array[i]
            write+=1
    return write, array[:write]

print(remove_duplicates_ii([1,1,2,2,2,3,4,5]))
    
