a=[0,2, 7]
b=[1, 3, 9]
t=[1, 22, 9, 4, 14, 12, 5 , 0]

def msort(c):
    if len(c)==1:
        return c
    else:
        m=len(c)//2
        a=msort(c[:m])
        b=msort(c[m:])
        return merge(a,b)

def merge(a,b):
    c=[]
    i=0
    j=0
    while i<len(a) or j<len(b):
        if i<len(a) and j<len(b):
            if a[i]<b[j]:
                c.append(a[i])
                i+=1
            else:
                c.append(b[j])
                j+=1
        elif i<len(a):
            c.append(a[i])
            i+=1
        elif j<len(b):
            c.append(b[j])
            j+=1
    return c

print(merge(a,b))
print(msort(t))

assert msort(t)==sorted(t)