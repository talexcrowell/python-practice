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
    if answer == "Y" or answer == 'y':
      choices[question] = True
    elif answer == "N" or answer == 'n':
      choices[question] = False
  
  print(choices)
  return choices

if __name__ == '__main__':
  ingredients_questions()