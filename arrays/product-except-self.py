def product_except_self(array):
    n=len(array)
    result=[1]*n

    left_product=1
    for i in range(n):
        result[i]=left_product
        left_product*=array[i]
    
    right_product=1
    for i in range(n-1,-1,-1):
        result[i]*=right_product
        right_product*=array[i]

    return result


print(product_except_self([1,2,3]))