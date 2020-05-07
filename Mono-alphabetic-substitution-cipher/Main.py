#   The mono-alphabetic substitution cipher (to encrypt and decrpt text)


#Predefine values
PDC = "XEUADNBKVMROCQFSYHWGLZIJPT"
PDP = "abcdefghijklmnopqrstuvwxyz"


def  Decryption(a):
    for i in range(len(PDC)):
        if a[0]==PDC[i]:
            print(PDP[i], end="")
            break

def Encription(a):
    for i in range(len(PDC)):
        if a[0]==PDP[i]:
            print(PDC[i], end="")
            break


#text to be decrpt
Text = "GDOOKVCXEFLGCD"

for i in range(len(Text)):
    Decryption(Text[i])
