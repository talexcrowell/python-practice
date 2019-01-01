import sys

print("The name of this script is {}".format(sys.argv[0]))
print("User supplied {} arguments at run time".format(len(sys.argv)))


if len(sys.argv) > 1:
  try:  
    n= int(sys.argv[1])
  except ValueError:
    print('Please retry with a numerical value')
    exit()
    
  
elif len(sys.argv) == 1:
  try:
    n = int(input('Enter a number to count to: '))
  except ValueError:
    print('Please retry with a numerical value')
    exit()

print('Fizz buzz counting up to {}:'.format(n))

for num in range(1,n+1):
  if num % 15 == 0:
    print('fizzbuzz')
  elif num % 5 ==0:
    print('buzz')
  elif num % 3 ==0:
    print('fizz')
  else:
    print(num)

