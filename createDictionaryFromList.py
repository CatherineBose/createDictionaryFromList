name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
  new_dict = {}
  arrLen = len(arr1)
  print "arrLen:", arrLen
  for i in range(0,arrLen):
    key = arr1[i]
    value = arr2[i]
    print "key ", key
    print "value ", value
    new_dict[key] = value
  # your code here
  print new_dict
  return new_dict

make_dict(name,favorite_animal)
