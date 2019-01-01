print ('Enter a number to count to:')
n = int(input())

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

