s=input("enter string you want to check: ")
flag=False
for i in range(len(s)//2):
    if(s[i]==s[(len(s)-1)-i]):
        flag=True
    else:
        flag=False
        break
if(flag==True):
    print("is pallindrome")
else:
    print("not palindrome")
