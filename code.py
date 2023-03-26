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
        b2=u2
        """if(len(b2)>0):
            continue"""
        if((b[0]=="O" and b[1]=="O" and b[2]=="O") or (b[3]=="O" and b[4]=="O" and b[5]=="O") or (b[6]=="O" and b[7]=="O" and b[8]=="O") or (b[0]=="O" and b[3]=="O" and b[6]=="O") or (b[1]=="O" and b[4]=="O" and b[7]=="O") or (b[2]=="O" and b[5]=="O" and b[8]=="O") or (b[0]=="O" and b[4]=="O" and b[8]=="O") or (b[6]=="O" and b[4]=="O" and b[2]=="O")):
            printgame(b)
            print("YOU WIN")
            break
        elif((b[0]=="X" and b[1]=="X" and b[2]=="X") or (b[3]=="X" and b[4]=="X" and b[5]=="X") or (b[6]=="X" and b[7]=="X" and b[8]=="X") or (b[0]=="X" and b[3]=="X" and b[6]=="X") or (b[1]=="X" and b[4]=="X" and b[7]=="X") or (b[2]=="X" and b[5]=="X" and b[8]=="X") or (b[0]=="X" and b[4]=="X" and b[8]=="X") or (b[6]=="X" and b[4]=="X" and b[2]=="X")):
            printgame(b)
            print("YOU LOSE")
            break
        elif(len(b2)>0):
            continue
        else:
            printgame(b)
            print("DRAW")
            break
            
        
elif(n=="X" or n=="x"):
    b=[1,2,3,4,5,6,7,8,9]
    b2=[1,2,3,4,5,6,7,8,9]
    p=True
    while(p):
        print("Choose your positon")
        printgame(b)
        y=0
        f=0
        k=int(input())
        b[k-1]="X"
        w=1
        while(w>0):
            m=random.choice(b2)
            if(m==k):
                w+=1
            else:
                break
        u2=[]
        b[m-1]="O"
        for j in range(len(b2)):
            if(b2[j]==m or b2[j]==k):
                pass
            else:
                u2.append(b2[j])
        b2=u2
        """if(len(b2)>0):
            continue"""
        if((b[0]=="O" and b[1]=="O" and b[2]=="O") or (b[3]=="O" and b[4]=="O" and b[5]=="O") or (b[6]=="O" and b[7]=="O" and b[8]=="O") or (b[0]=="O" and b[3]=="O" and b[6]=="O") or (b[1]=="O" and b[4]=="O" and b[7]=="O") or (b[2]=="O" and b[5]=="O" and b[8]=="O") or (b[0]=="O" and b[4]=="O" and b[8]=="O") or (b[6]=="O" and b[4]=="O" and b[2]=="O")):
            printgame(b)
            print("YOU LOSE")
            break
        elif((b[0]=="X" and b[1]=="X" and b[2]=="X") or (b[3]=="X" and b[4]=="X" and b[5]=="X") or (b[6]=="X" and b[7]=="X" and b[8]=="X") or (b[0]=="X" and b[3]=="X" and b[6]=="X") or (b[1]=="X" and b[4]=="X" and b[7]=="X") or (b[2]=="X" and b[5]=="X" and b[8]=="X") or (b[0]=="X" and b[4]=="X" and b[8]=="X") or (b[6]=="X" and b[4]=="X" and b[2]=="X")):
            printgame(b)
            print("YOU WIN")
            break
        elif(len(b2)==0):
            if((b[0]=="O" and b[1]=="O" and b[2]=="O") or (b[3]=="O" and b[4]=="O" and b[5]=="O") or (b[6]=="O" and b[7]=="O" and b[8]=="O") or (b[0]=="O" and b[3]=="O" and b[6]=="O") or (b[1]=="O" and b[4]=="O" and b[7]=="O") or (b[2]=="O" and b[5]=="O" and b[8]=="O") or (b[0]=="O" and b[4]=="O" and b[8]=="O") or (b[6]=="O" and b[4]=="O" and b[2]=="O")):
                printgame(b)
                print("YOU LOSE")
                break
            elif((b[0]=="X" and b[1]=="X" and b[2]=="X") or (b[3]=="X" and b[4]=="X" and b[5]=="X") or (b[6]=="X" and b[7]=="X" and b[8]=="X") or (b[0]=="X" and b[3]=="X" and b[6]=="X") or (b[1]=="X" and b[4]=="X" and b[7]=="X") or (b[2]=="X" and b[5]=="X" and b[8]=="X") or (b[0]=="X" and b[4]=="X" and b[8]=="X") or (b[6]=="X" and b[4]=="X" and b[2]=="X")):
                printgame(b)
                print("YOU WIN")
                break
            else:
                printgame(b)
                print("DRAW")
                break
        elif(len(b2)>0):
            continue
        else:
            printgame(b)
            print("DRAW")
            break
    
else:
    print("PLAYER CHOICE IS UNAVAILABLE")
          
    
