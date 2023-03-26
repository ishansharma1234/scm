import random

print("Choose a player: O or X")
n=input()
def printgame(a):
    print(a[0]," | ", a[1]," | ", a[2])
    print("-","-|-","-","-|-","-")
    print(a[3]," | ", a[4]," | ", a[5])
    print("-","-|-","-","-|-","-")
    print(a[6]," | ", a[7]," | ", a[8])
    

if(n=="O" or n=="o"):
    b=[1,2,3,4,5,6,7,8,9]
    b2=[1,2,3,4,5,6,7,8,9]
    p=True
    while(p):
        print("Choose your positon")
        printgame(b)
        y=0
        f=0
        k=int(input())
        b[k-1]="O"
        w=1
        while(w>0):
            m=random.choice(b2)
            if(m==k):
                w+=1
            else:
                break
        u2=[]
        b[m-1]="X"
        for j in range(len(b2)):
            if(b2[j]==m or b2[j]==k):
                pass
            else:
                u2.append(b2[j])
