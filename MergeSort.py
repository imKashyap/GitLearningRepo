def mergeSort(seq, left, right):
    
    def mergeList(seq, left, mid, right):
        a = []
        i = left
        j = mid
        while i<=mid-1 or j<=right:
           
            if i==mid-1 and j == right:
                break
            elif seq[i]<seq[j]:
               a.append(seq[i])
               i += 1
            elif seq[j] < seq[i]:
                a.append(seq[j])
                j += 1
            elif i == mid-1 :
                a.append(seq[j])
                j += 1
            elif j == left :
                a.append(seq[i])
                i += 1
        seq = [i for i in range(left, right+1)]
         
    
    mid = (left + right)//2
    if mid == left:
        return
    else:
        mergeSort(seq, left, mid-1)
        mergeSort(seq, mid, right)
        mergeList(seq, left, mid, right)
        
    
seq = [3,1,5,3,63,5,2,78,5,4,8,53,6,3,7,9,0,8,5,33,32,76]
print(seq)
mergeSort(seq,0, len(seq)-1)
print(seq)