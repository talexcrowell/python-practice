phone_book = {
  "sarah hughes": "01234 567890",
  'tim taylor': "02345 678901",
  'sam smith': '03456789012'
}

try:
  'Jamie Theakston' in phone_book
  print(phone_book['Jamie Theakston'])
except KeyError:
  print('Not in this phonebook')

try:
  print(phone_book['tim taylor'])
except KeyError:
  print('Not in this phonebook')
