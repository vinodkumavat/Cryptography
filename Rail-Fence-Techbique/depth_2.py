# Rail Fence technique (for depth 2)
def Encryption(text):
    str1 = ""
    str2 = ""
    for i in range(len(text)):
        if i % 2 == 0:
            str1 = str1 + text[i]
        else:
            str2 = str2 + text[i]
    return (str1+str2)


def Decrption(text):
    str1 = ""
    str2 = ""
    str3 = ""
    if len(text) % 2 != 0:
        # getting 2 different string
        for i in range(len(text)):
            if i <= (len(text)//2):
                str1 = str1 + text[i]
            else:
                str2 = str2 + text[i]

        # adding into one string alternatively
        for k in range(len(str1)):
            str3 = str3 + str1[k]
            if k < len(str2):
                str3 = str3 + str2[k]
    return str3


print(Encryption("how are you ?"))
print(Decrption(Encryption("how are you ?")))
