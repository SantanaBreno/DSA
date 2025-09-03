import insertion_sort

def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    
    # Put array elements in different buckets
    for num in arr:
        bi = int(n * num)
        buckets[bi].append(num)
        
    # Sort individual buckets using insertion sort   
    for bucket in buckets:
        insertion_sort(bucket)
        
    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1
            
    return arr