inw, out = 0, 0

for i in range(int(input())):
  X = int(input())
  if(X >= 10 and X <= 20): inw += 1
  else: out += 1

print(inw, "in")
print(out, "out")