a = [1,2,3,4,5,6,7]
start = 0
mid  = 0
key = 5
end = len(a)-1
while(start<=end):
    mid =(start+end)//2
    if(key<a[mid]):
        end = mid-1
    elif(key>a[mid]):
        start = mid+1
    else:
        print(mid)
        break