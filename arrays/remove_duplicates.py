#Sorted duplicates
def remove_duplicates(array):
    if not array:
        return 0
    write=1
    for i in range(1,len(array)):
        if array[i]!=array[i-1]:
            array[write]=array[i]
            write+=1
    return array[:write],write
print(remove_duplicates([1,1,2,2,3,4,4]))
        
        