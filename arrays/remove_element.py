def remove_element(array,val):
    element_remove=0
    for i in range(len(array)):
        if array[i]!=val:
            array[element_remove]=array[i]
            element_remove+=1

    return element_remove

# print(remove_element([2,3,1,3],3))
nums=[2,3,1,3,5,1]
k=remove_element(nums,3)
print(nums[:k])
print(k)
