print('___________fibonacci ___________')
n=int(input('How many elements do you want from the Fibonacci series?'))
f0,f1 =0 , 1
li=[0,1]
for i in range(2,n):
    f2=f0+f1
    li.append(f2)
    f0=f1
    f1=f2

print(li)
