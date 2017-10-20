t=int(input(""))

while t>=1:

    n=int(input(""))
    sl=input().split()
    val= "Yes"
    x=0

    #seleccionar la cota superior del conjunto
    if int(sl[-1])>int(sl[0]):
        x=int(sl.pop(-1))
    elif int(sl[0])>int(sl[-1]):
        x=int(sl.pop(0))
    else:
        x=int(sl.pop(-1))
        if len(sl)>=2:
                y=int(sl.pop(0))

    #apilador de cubos
    for i in range(1,len(sl)+1):
        if len(sl)==1:
            if x<int(sl[0]):
                val="No"
                print(val)
            break

        if x>=int(sl[0]):
            if int(sl[0])== int(sl[-1]):
                x=int(sl.pop(0))
                if len(sl)>=2:
                    y=int(sl.pop(-1))
            elif (x==int(sl[0])) or (int(sl[0])>int(sl[-1])):
                x=int(sl.pop(0))
            elif x>=int(sl[-1])>int(sl[0]):
                x=int(sl.pop(-1))
            else:
                val="No"
                break

        elif x>=int(sl[-1]):
            if int(sl[-1])== int(sl[0]):
                x=int(sl.pop(-1))
                if len(sl)>=2:
                    y=int(sl.pop(0))
            elif (x==int(sl[-1])) or (int(sl[-1])>int(sl[0])):
                x=int(sl.pop(-1))
            elif x>=int(sl[0])>=int(sl[-1]):
                x=int(sl.pop(0))
            else:
                val="No"
                break
        else:
            val="No"

            break
    print(val)
    t-=1
    
