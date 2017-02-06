a = [1,3,5,6,6,9]
n = 6
sum = 16
result = "N"

for i in range(n):
    for j in range(n):
        if a[i] + a[j] == sum:
             result = "Y"
             break
    if result == "Y":
        break
if result == "Y":
    print(result,i,j,a[i],a[j])
else:
    print(result)
