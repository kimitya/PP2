import re
text = input()
pattern = "t.*t"
x = re.search(pattern, text)

print (x)