import collections
a = [1,1,2,3,3,2,5]
f = {}
# frequency = collections.Counter(a)
# print(dict(frequency))
for item in a:
    if item in f:
        f[item]+=1
    else:
        f[item]=1
for key,value in f.items():
    if value == 1:
         print(key)
