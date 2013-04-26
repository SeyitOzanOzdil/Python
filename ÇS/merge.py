def merge (alist1,alist2):
    toplam = len(alist1)+len(alist2)
    alist = [0]*toplam
    i,j,k = 0,0,0
    while i<len(alist1) and j<len(alist2):
        if alist1[i] < alist2[j]:
            alist[k] = alist1[i]
            i += 1
        else:
            alist[k] = alist2[j]
            j += 1
        k += 1

    while i<len(alist1):
        alist[k]=alist1[i]
        i += 1
        k += 1

    while j<len(alist2):
        alist[k]=alist2[j]
        j += 1
        k += 1

    print "Merging", alist
            
    
