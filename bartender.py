import random

questions = {
  "strong":"Do ye like yer drinks strong?",
  "salty": "Do ye like it with a salty tang?",
  "bitter": "Are ye a lubber who likes it bitter?",
  "sweet": "Would ye like a bit of sweetness with yer poison?",
  "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
  "strong": ["glug of rum", "slug of whisky", "splash of gin"],
  "salty": ["olive on a stick", "salt dusted rim", "rasher of bacon"],
  "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
  "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
  "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def ingredients_questions():
  '''This function asks the user what kind of ingredients the want in their pirate cocktail'''
  choices = {}
  for question in questions:
    answer = input(questions[question] + ": ")
    if answer == "Y" or answer == 'y' or answer == 'Yes' or answer == 'yes':
      choices[question] = True
    elif answer == "N" or answer == 'n' or answer == 'No' or answer == 'no':
      choices[question] = False
    else:
      print('Give me a quick yes or no (y/n)! I don\'t have time for your life story! Anyways...')
  return choices

def make_drink(choices):
  '''This function returns a drink based off the users choices of flavors'''
  drink =[]
  for choice in choices:
    if choices[choice] == True:
      drink.append(random.choice(ingredients[choice]))
  return drink
      
def bartender():
  '''This function combines the ingredients_questions and make_drink functions''' 
  choices = ingredients_questions()
  drink = make_drink(choices)
  name = input("Name ye drink, matey!: ")
  print("A {} made with {}".format(name, drink))


if __name__ == '__main__':
  bartender()