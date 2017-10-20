N, K= list(map(int,input().strip().split()))

CNumb=[]
ICL=[]
A=0
add=0
for i in range(N):
    CNumb+=[list(map(int,input().strip().split()))]


for j in range(N):
    if CNumb[j][1]==1:
        ICL+=[CNumb[j][0]]

    else:
        add+=CNumb[j][0]

ICL.sort()


for w in range(len(ICL)):
    if K>=1:
        add+=int(ICL[-1-w])
        K-=1
        A+=1
    else:
        add-=int(ICL[0+(w-A)])

print(add)

# 10 3
# 3 1
# 13 1
# 21 1
# 31 1
# 17 1
# 20 1
# 8 1
# 12 0
# 14 0
# 21 1
# 38
