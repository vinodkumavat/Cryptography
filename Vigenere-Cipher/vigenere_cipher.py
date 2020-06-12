Alpha = "abcdefghijklmnopqrstuvwxyz"
Key = "cafe"
PT = "tellhimaboutme"
CT = "veqpjiredozxoe"

def Encription(a, k):
    for i in range(len(Alpha)):
        if a[0]==Alpha[i]:
            for j in range(len(Alpha)):
                if Key[k]==Alpha[j]:
                    print(Alpha[i+j], end="")
                    break
            break

def Decrption(a, k):
    for i in range(len(Alpha)):
        if a[0]==Alpha[i]:
            for j in range(len(Alpha)):
                if Key[k]==Alpha[j]:
                    print(Alpha[i-j], end="")
                    break
            break



#For decrption of Plane Text
k=0
for i in range(len(PT)):
    Encription(PT[i], k)
    k=k+1
    #for repeating key if lenght is smaller than PlaneText or CipherText
    if k==len(Key):
        k=0


#For decrption of Cipher Text
print()
k=0
for i in range(len(PT)):
    Decrption(CT[i], k)
    k=k+1
    #for repeating key if lenght is smaller than CipherText
    if k==len(Key):
        k=0
