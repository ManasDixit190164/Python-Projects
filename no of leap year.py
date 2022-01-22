def leapyear(n):
    if (n%100!=0 and n%4==0):
        return n
    elif n%400==0:
        return n

start=int(input("Starting Year:- "))
end=int(input("End Year:- "))
a=[]
for i in range(start,end+1):
    if leapyear(i):
        a.append(i)
print(a)