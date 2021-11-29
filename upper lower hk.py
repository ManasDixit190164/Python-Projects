
s="HackerRank.com"
# m = str(m)
m=""
for i in s:
    if i.isupper():
        m=m+ i.lower()
    elif i.islower():
        m=m+ i.upper()
    else:
        m=m+i
print(m)