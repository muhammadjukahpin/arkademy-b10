def pattern(input):
  if input % 2 == 1:
    for i in range(input):
      print()
      for j in range(input):
        if (i==j) or (input-i-1==j):
  	      print('X', end=" ")
        else:
          print('=', end=" ")
    print()
  else:
  	print("Harus angka ganjil.")
pattern(7)