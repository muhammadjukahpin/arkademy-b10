def cetak_gambar(x):
  if (x%2 == 1):
    for i in range(x):
      for j in range(x):
        if (j == x//2):
          print('x', end=" ")
        else:
          if (i == 0) or (i == x-1):
            print('x', end=" ")
          else:
            print('=', end=" ")
      print("\n")
  else:
    print("Failed")

cetak_gambar(7)