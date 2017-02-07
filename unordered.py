a = [5,3,7,4,9,1]
sum = 11

have = False
b = {sum - a[0]:0}
for i in range(1,len(a)):
    if a[i] in b.keys():
        have = True
        break
    else:
        b[sum - a[i]] = i

if have:
    print("Y")
    print("Position:",b[a[i]],i)
    print("Value:",sum - a[i],a[i])
else:
    print("N")
