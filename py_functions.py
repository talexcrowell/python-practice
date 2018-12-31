def subtractor(a,b):
  '''I subtract b from a and return the result'''
  print("I'm a function. My name is {}".format(subtractor.__name__))
  print("I'm about to subtract {} and {} \n...\n...". format(a,b))
  return a-b

def print_function():
  '''I'm also a function, but I don't take any parameters'''
  print("I'm {}, and I'm printing now".format(print_function.__name__))

def function3(a=55, b=22):
  '''I'm a function that calls other functions'''
  print("I'm {} and I'm about to call subtractor function".format(function3.__name__))
  total = subtractor(a,b)
  print("I'm {} and I'm about to call print_function".format(function3.__name__))
  print_function()
  print("I'm {} and I'm about to return total".format(function3.__name__))
  return total

def side_effect_test(value):
  value[1] = 'orange'
  print("Inside the function, the value becomes {}".format(value))


if __name__ == '__main__':
  value = ['red', 'blue', 'white']
  print('Outside the function, the value starts as {}'.format(value))
  side_effect_test(value)
  print('Outside the function, the value is now {}'.format(value))
