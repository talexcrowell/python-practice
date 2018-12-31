def subtractor(a,b):
  '''I subtract b from a and return the result'''
  print("I'm a function. My name is {}".format(subtractor.__name__))
  print("I'm about to subtract {} and {} \n...\n...". format(a,b))
  return a-b

def print_function():
  '''I'm also a function, but I don't take any parameters'''
  print("I'm {}, and I'm printing now".format(print_function.__name__))

if __name__ == '__main__':
  print_function()