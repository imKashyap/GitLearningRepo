
def insertionSort(seq):
    for sortedEnd in range(len(seq)):
        pos = sortedEnd
        while ((pos > 0) and (seq[pos] < seq[pos - 1])): 
            (seq[pos], seq[pos - 1]) = (seq[pos - 1], seq[pos])
            pos = pos - 1
            
            
seq = [3,1,5,3,63,5,2,78,5,4,8,53,6,3,7,9,0,8,5,33,32,76]
print(seq)
insertionSort(seq)
print(seq)
        