a = [1,3,5,6,6,9]
sum = 11

low = 0
high = len(a) - 1
while low < high:
    total = a[low]+a[high]
    if total ==sum:
        break
    elif total < sum:
        low += 1
    else:
        high -= 1

if total == sum:
    print("Y")
    print("Position:",low,high)
    print("Value:",a[low],a[high])
else:
    print("N")
