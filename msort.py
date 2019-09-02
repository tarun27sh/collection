def merge(arr, lo, mid, hi):
    l1 = arr[lo:mid+1]
    l2 = arr[mid+1:hi+1]
    i = lo
    l1_index =  l2_index = 0
    while l1_index < len(l1) and l2_index < len(l2):
        if l1[l1_index] < l2[l2_index]:
            arr[i] = l1[l1_index]
            l1_index += 1
        else:
            arr[i] = l2[l2_index]
            l2_index += 1
        i+=1
    while l1_index < len (l1):
        arr[i] = l1[l1_index]
        i+=1
        l1_index+=1
    while l2_index < len (l2):
        arr[i] = l2[l2_index]
        i+=1
        l2_index+=1

def mergesort(arr, lo, hi):
    print('lo={}, hi={}'.format(lo, hi))
    if lo == hi:
        return
    mid = (lo + hi ) // 2
    mergesort(arr, lo, mid)
    mergesort(arr, mid+1, hi)
    merge(arr, lo, mid, hi)
    





li = [x for x in range(100, 0, -1)]
mergesort(li, 0, len(li)-1)
print(li)
