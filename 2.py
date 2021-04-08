n=int(input('Please enter the length of the first set:'))
l1=[]
for m in range(n):
    b=int(input('cell '+str(m)))
    l1.append(b)

un=int(input('Please enter the length of the second set:'))
l2=[]
for m in range(un):
    cb=int(input('cell '+str(m)))
    l2.append(cb)
print('Collection A: ',set(l1))
print('Collection B: ',set(l2))
set1=set(l1)
set2=set(l2)

print('Community: ',set1.union(set2))
print('Subscription: ',set1.intersection(set2))
