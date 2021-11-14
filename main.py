#Number Guessing Game Objectives:
logo="""
 $$$$$$\                                                 $$\     $$\                                                         $$\                           
$$  __$$\                                                $$ |    $$ |                                                        $$ |                          
$$ /  \__|$$\   $$\  $$$$$$\  $$$$$$$\  $$$$$$$\       $$$$$$\   $$$$$$$\   $$$$$$\        $$$$$$$\  $$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$ |$$$$\ $$ |  $$ |$$  __$$\$$  _____|$$  _____|      \_$$  _|  $$  __$$\ $$  __$$\       $$  __$$\ $$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ |\_$$ |$$ |  $$ |$$$$$$$$ \$$$$$$\  \$$$$$$\          $$ |    $$ |  $$ |$$$$$$$$ |      $$ |  $$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |  $$ |$$   ____|\____$$\  \____$$\         $$ |$$\ $$ |  $$ |$$   ____|      $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$  |\$$$$$$  |\$$$$$$$\$$$$$$$  |$$$$$$$  |        \$$$$  |$$ |  $$ |\$$$$$$$\       $$ |  $$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |      
 \______/  \______/  \_______\_______/ \_______/          \____/ \__|  \__| \_______|      \__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|      
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
"""
def gamer(no_of_options):
  is_game_over=True
  while no_of_options!=0 and is_game_over==True:
    print(f"You have {no_of_options} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if guess>answer:
      print("Too high")
      print("Guess again")
    elif guess<answer:
      print("Too less")
      print("Guess again")
    elif guess==answer:
      print("you found the number!!!")
      is_game_over=False
    no_of_options-=1
print(logo)
import random

print("Welcome to the Number Guessing Game! \
I'm thinking of a number between 1 and 100. ")
choice=input("Choose a difficulty. Type 'easy' or 'hard': \n")
answer=random.randint(1,100)
print(f"answer is {answer}")
if choice=="easy":
  no_of_options=10
  gamer(no_of_options)
else:
  no_of_options=5  
  gamer(no_of_options)
  
    