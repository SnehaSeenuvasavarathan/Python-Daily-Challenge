arr=[1, 8, 19, 15, 2, 29, 3, 2, 25, 2, 19, 26, 17, 33, 22]
k=20
ct=0
pg=1
pb=1
ch=0
while(ch<len(arr)):
    if pg>=pb and pg<=min(pb+k-1,arr[ch]):
        ct+=1
    pg+=1
    pb+=k
    if pb>arr[ch]:
        pb=1
        ch+=1
print(ct)