import random

# ASCII Art for Elements
fire = '''
    (  )
   ( )(
    (  )
     ( )
      V
'''

wind = '''
  ,___,
  [O.o]
  /)__)
--"-"---
'''

lightning = '''
   /\\
  //\\\\
  \\\\
'''

earth = '''
  /\\
 /  \\
/____\\
'''

water = '''
   ~~
  ~~~~
 ~~~~~~
'''

game_images = [fire, wind, lightning, earth, water]

# Get user choice
user_choice = int(input("What do you choose? Type 0 for Fire, 1 for Wind, 2 for Lightning, 3 for Earth, or 4 for Water.\n"))
if user_choice >= 5 or user_choice < 0:
    print("You typed an invalid number, you lose!") 
else:
    print(game_images[user_choice])

    # Get computer choice
    computer_choice = random.randint(0, 4)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw")
    elif (user_choice == 0 and computer_choice == 1) or \
         (user_choice == 1 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 3) or \
         (user_choice == 3 and computer_choice == 4) or \
         (user_choice == 4 and computer_choice == 0):
        print("You win!")
    else:
        print("You lose")
