def two_sum(array,target):
    seen={}
    for i, num in enumerate(array):
        need=target-num
        if need in seen:
            return f"pos:{[seen[need],i]} , values:{[need , num]}"
        seen[num]=i
    return []

print(two_sum([7,8,9],15))