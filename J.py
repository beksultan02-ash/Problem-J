
def isAnagram(str1,str2):
    return sorted(str1) == sorted(str2)

str1 = input()
str2 = input()

if isAnagram(str1,str2):
    print("YES")
else:
    print("NO")