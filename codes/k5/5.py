def ganti_kata(word,charTarget,charChange):
  convert = list(word)
  convertLength = len(convert)
  for i in range(convertLength):
  	if convert[i] == charTarget:
  	  convert[i] = charChange
  word = "".join(convert)
  print(word)

ganti_kata('Purwakarta','a','o')