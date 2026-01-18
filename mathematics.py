try:
  a = float(input("Enter first number:"))
  b = float(input("Enter second number:"))
  print(f"Addition:{a+b}")
  print(f"subtraction:{a-b}")
except valueError:
  print("please enter valid numbers")
