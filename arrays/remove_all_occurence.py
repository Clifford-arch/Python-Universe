"""Remove all occurence of a val in array """
def remove_all_occurrence(array,val):
   left=0
   right=len(array)-1
   while left<=right:
    if array[left]==val:
        array[left],array[right]=array[right],array[left]
        right-=1
    else:
        left+=1
   return right+1,array[:right+1]

print(remove_all_occurrence([1,2,2,3,4,2,2],2))