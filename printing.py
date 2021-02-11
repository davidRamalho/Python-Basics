array = ['bob', 'eric', 'boobies']

array.append('people')
print(array)
array.remove('people')
print(array)

for item in array:
  array.remove(item)
  print(array)
  
for item in array:
  array.remove(item)
  print(array)
    
print(array)