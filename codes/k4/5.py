data = ['h','g','a','b','d','f']
datalain = ['a','b','c','d']

def compare(array,lesserIndex,greaterIndex):
  while array[lesserIndex] > array[greaterIndex]:
  	del array[lesserIndex]
  return array

def sorter(array):
  first    = 0
  second   = 1
  elements = len(array)
  while second < elements:
    compare(array,first,second)
    first += 1
    second += 1
    elements = len(array)
  return array

def minmax(array):
  sorter(array)
  elements = len(array)
  newArray = [array[0],array[elements-1]]
  print(newArray)

minmax(datalain)