import math
from unittest import result

string = "Hello"
key = "world"

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    tes = (str(bin(i)[2:]))
    if (len(tes) < 8):
        tes = "0" + tes
    #print(tes)
    m.append(tes)
  return m

# print(toBinary("Hello world"))
binary_string = ''.join(toBinary(string))
binary_key = ''.join(toBinary(key))

print(binary_string)
print(binary_key)

result = int(binary_string) ^ int(binary_key)
print(result)