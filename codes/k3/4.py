karakter=["P","R","O","G","R","A","M","M","E","R"]
def jolly_roger():
  for i in range(len(karakter)):
    print()
    for j in range(len(karakter)):
      if (i==j) or (i+j==9):
  	    print(karakter[i], end=" ")
      else:
        print('=', end=" ")
  print()
jolly_roger()