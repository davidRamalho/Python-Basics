def uppercase_and_reverse(word):
  result = ""
  word = word.upper()
  word = list(reversed(word))
  
  for letter in word: 
    result += letter
  return result

print(uppercase_and_reverse("banana"))