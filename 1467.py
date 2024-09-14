while True:
  try:
    A, B, C = map(int, input().split())

    elif A == B:
      print("C")
    elif A == C:
      print("B")
    elif B == C:
      print("A")
    else:
      print("*")

  except EOFError:
    break