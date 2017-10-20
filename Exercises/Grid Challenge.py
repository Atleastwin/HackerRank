T=int(input())

for tcases in range(T):
    N=int(input())
    arr=[]
    arr3=[]
    arr5=[]

    for i in range(N):
        arr1=list(input().strip())
        print(arr1)
        arr1.sort()
        arr+=[arr1]

    for i in range(N):
        arr2=[]
        arr4=[]
        for j in range(N):
            arr2+= arr[j][i]
            arr4+= arr[j][i]
            arr4.sort()
        arr3+=[arr2]
        arr5+=[arr4]


    if arr3==arr5:
        print("YES")
    else:
        print("NO")
