a = [1,3,5,6,6,9]
n = 6
sum = 11

def search(a,difference):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(low+high)//2
        if a[mid]==difference:
            return mid
        elif a[mid]<difference:
            low=mid+1
        else:
            high=mid-1
    return -1

for i in range(n):
    difference = sum - a[i]
    index = search(a,difference)
    if index != -1:
        break

if index != -1:
    print("Y",i,index,a[i],a[index])
else:
    print("N")
