a = [1, 4, 2, 10, 5, 0, 3]
acopy = a
print(a)
sort_more=True
while sort_more:
    sort_more=False
    for i in range(1,len(a)):
        if a[i]<a[i-1]:
            a[i],a[i-1]=a[i-1],a[i]
            sort_more=True
print(a)
assert a==sorted(acopy)


