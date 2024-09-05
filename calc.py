import sys
fin=open("input.txt","rt")
sys.stdin=fin
fout=open("output.txt","wt")
sys.stdout=fout
while True:
    parts=input().strip().split()
    parts[1]=int(parts[1])
    parts[2]=int(parts[2])
    if parts[0]=="add":
        print(parts[1]+parts[2])
    elif parts[0]=="sub":
        print(parts[1]-parts[2])    
    elif parts[0]=="mul":
        print(parts[1]*parts[2])   
    elif parts[0]=="truediv":
        print(parts[1]/parts[2])
    elif parts[0]=="floordiv":
        print(parts[1]//parts[2])
    elif parts[0]=="mod":
        print(parts[1]%parts[2])    
    elif parts[0]=="pow":
        print(parts[1]**parts[2])
