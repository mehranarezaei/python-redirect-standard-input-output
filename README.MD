# how to redirect standard input output
to import from input and write to output use `sys`
```python
import sys
```
this is how you read from input in file named input.txt:
```python
fin=open("input.txt","rt")
sys.stdin=fin
```
this is how you write the output and name it to output.txt:
```python
fout=open("output.txt","wt")
sys.stdout=fout
```
and then you have to merge all together in a code.

as an example here is a snippet code for adding two numbers:
```python
import sys
fin=open("input.txt","rt")
sys.stdin=fin
fout=open("output.txt","wt")
sys.stdout=fout
while True:
    parts=input().strip().split()
    if parts[0]=="add":
        print(int(parts[1])+int(parts[2]))
```