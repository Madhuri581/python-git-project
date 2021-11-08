def ispalindrome(s):
    return s==s[::-1]
s="mom"
ans=ispalindrome(s)
if ans:
   printf("yes")
else:
   printf("no")