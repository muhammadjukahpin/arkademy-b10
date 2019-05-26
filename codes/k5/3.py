def count_vowels(stringInput):
  stringLength= len(stringInput)
  count = 0
  for z in range(0,stringLength):
    i   = stringInput[z] == 'a'
    ii  = stringInput[z] == 'i'
    iii = stringInput[z] == 'u'
    iv  = stringInput[z] == 'e'
    v   = stringInput[z] == 'o'
    if  i or ii or iii or iv or v:
      count += 1
  print(count)

count_vowels("bootcamp")
count_vowels("arkademy")
count_vowels("programmer")
count_vowels("hmm...")