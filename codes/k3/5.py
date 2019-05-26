data=[['a','c','b','e','d'],['g','e','f'],['h','i','j','k']]

def sort_array(input):
  elements = len(input)
  for i in range(0,elements):
    childs = len(input[i])
    if (childs>1):
      for j in range(childs):
        for k in range(0,childs-j-1):
          if (input[i][k] < input[i][k+1]):
            input[i][k], input[i][k+1] = input[i][k+1], input[i][k]
  return(input)

def biggest_branch(input):
  sort_array(input)
  biggest = []
  elements= len(input)
  for i in range(0,elements):
    biggest.append(input[i][0])
  print(biggest)

biggest_branch(data)