import math

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(str(bin(i)[2:]))
  return m

#print(toBinary("Hello world"))
yes = ''.join(toBinary("Hello"))
print(yes)