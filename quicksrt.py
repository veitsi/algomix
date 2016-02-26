def quick00(start,end):
    if end-start<1:
        return
    if end-start==1:
        if a[start]>a[end]:
            a[start],a[end]=a[end],a[start]
        return
    pi=(end+start)//2
    pivot=a[pi]
    i,j=start,end
    while True:
        while a[i]<a[pi] or i<pi:
            i+=1
        while a[j]>a[pi] or j>pi:
            j-=1
        if i==j:
            break
        if i<pi<j:
            print (i,j)
            a[i],a[j]=a[j],a[i]
            continue
        print (i,j)
        print(a)
        if i<pi:
            a[i],a[pi]=a[pi],a[i]
            pi=j
        if j>pi:
            a[pi],a[j]=a[j],a[pi]
            pi=i

    quick(start,pi-1)
    quick(pi+1,end)
    return pi,pivot

a = [None, 1, 9, 4, 12, 10]
print(quick00(1,len(a)-1))
print(a)

