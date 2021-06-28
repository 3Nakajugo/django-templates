import sys


def uncensor(string, vowels):
  counter = 1
  new_sting = " "
  for letter in string:
    print (letter)
    if letter == '*':
      new_sting+= vowels[counter]
      counter += 1
    else :
      new_sting += letter
  return new_sting
  
  

args = []
for line in sys.stdin:
 args.append(line)
 
string, vowels = args
 
print(uncensor(string, vowels))