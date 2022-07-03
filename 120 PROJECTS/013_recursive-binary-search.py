def rec_binarySearch(target, sequence, first, last):
    if first > last:
        return False
    # else:
    #     mid = (last + first)
    #     if sequence[mid]==target:
    #         return True
    #     elif(target < sequence[mid]):
    #         return rec_binarySearch(target,sequence,first,mid-1)
    #     else:
    #         return rec_binarySearch(target,sequence,mid+1,last)
target=[34,45,12,5,6,4,45,24,456]
sequence=target.sort()
first=34
last=2
rec_binarySearch(target,sequence,first,last)