while True:
  A = input().split()
  if(A = ['0', '0', '0', '0']): break

  Xdama, Ydama, Xobj, Yobj = map(int, A)

  if Xdama == Xobj and Ydama == Yobj:
    print("0")
  elif (Xdama == Xobj or Ydama == Yobj) or (abs(Xdama - Xobj) == abs(Ydama - Yobj)):
    print("1")
  else:
    print("2")