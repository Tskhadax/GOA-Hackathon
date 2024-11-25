string = "gurami"
xmovnebi = "aeiou"
 
s = 0

for elements in string:
   for i in xmovnebi:
    if elements == i:
      s += 1
print(s)