#1,2,3,4,5
arr     = [9,5,8,4,3,6]
i       = 0
next    = i + 1
len     = len(arr)
for i in range(len):
    for next in range(i,len):
        if arr[i] > arr[next]:
            temp        = arr[next]
            arr[next]   = arr[i]
            arr[i]      = temp
        next = next + 1
print(arr)