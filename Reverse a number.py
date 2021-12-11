n = 12345
rv = 0
rm = 0
while n!=0:
    rm=n%10
    rv=(rv*10)+rm
    n=n//10
print(rv)