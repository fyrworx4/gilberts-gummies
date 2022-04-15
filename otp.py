import math

string = "Hello"
key = "world"

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(str(bin(i)[2:]))
  return m

#print(toBinary("Hello world"))
binary_string = ' '.join(toBinary(string))
binary_key = ' '.join(toBinary(key))

print(binary_string)
print(binary_key)