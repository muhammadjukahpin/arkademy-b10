def myCountChar(stringInput,charInput):
  stringLength= len(stringInput)
  count = 0
  for i in range(0,stringLength):
    if stringInput[i] == charInput:
      count += 1
  print(count)

myCountChar("bootcamp","o")
myCountChar("arkademy","k")