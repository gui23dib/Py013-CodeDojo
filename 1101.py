while True:
  X = [int(e) for e in input().split()]
  if 0 in X: break

  sum = 0
  X.sort() 
  for i in range(X[0], X[1] + 1):
    sum += i
    print(i, end=" ")

  print(f"Sum={sum}")