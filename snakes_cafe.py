import sys


print('**************************************\n'
'**    Welcome to the Snakes Cafe!   **\n'
'**    Please see our menu below.    **\n'
'**\n'
'** To quit at any time, type "quit" **\n'
'**************************************')

print('Appetizers\n'
'----------\n'
'Wings\n'
'Crab Rangoon\n'
'Sliders\n'

'Entrees\n'
'-------\n'
'Tacos\n'
'Pizza\n'
'Tikka Masala\n\n'

'Desserts\n'
'--------\n'
'Ice Cream\n'
'Mochi\n'
'Cookies\n\n'

'Drinks\n'
'------\n'
'Iced Coffee\n'
'Hot Chocolate\n'
'Tea\n')


menu = {
  'Crab Rangoon' : 0,
  'Wings' : 0,
  'Sliders' : 0,
  'Tacos' : 0,
  'Pizza' : 0,
  'Tikka Masala' : 0,
  'Ice Cream' : 0,
  'Mochi' : 0,
  'Cookies' : 0,
  'Iced Coffee' : 0,
  'Hot Chocolate' : 0,
  'Tea' : 0
}

def exit():
  print('All Done!')
  sys.exit()

while True:
  answer = input('**************************************\n'
    '** What would you like to order? **\n'
    '**************************************\n')

  if answer == 'quit':
    exit()

  if answer in menu:
    menu[answer] += 1
    print(f'{menu[answer]} order of {answer} has been added to your order\n')

  else:
    print('Sorry, we don\'t have that available')
