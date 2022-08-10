# import random
#
#
#
# comp=print('Computer Turn: Rock(R),Paper(P) or Scissor(S),\n(The computer has chosen it\'s choice secretly) ')
# rand=random.randint(1,3)
# if rand==1:
#     comp='R'
# elif rand==2:
#     comp='P'
# elif rand==3:
#     comp='S'
# p2=input('Your choice: Rock(R),Paper(P) or Scissor(S):')
#
#
#
# def gamewin(comp,p2):
#     if comp==p2:
#         return False
#     elif comp=='R':
#         if p2=='P':
#             return True
#         elif p2=='S':
#             return False
#
#     elif comp=='P':
#         if p2=='R':
#             return False
#         elif p2=='S':
#             return True
#
#     elif comp=='S':
#         if p2=='R':
#             return True
#         elif p2=='P':
#             return False
#
#
# a=gamewin(comp,p2)
# if comp==p2:
#     print('The game is a tie')
#
# elif a:
#     print('You won the game congratulations')
#
# else :
#     print('You lost the game,better luck next time')
#
# print(f'The computer chose {comp}')
# print(f'The player chose {p2}')


#Project 2 (GOOD LUCK)
# import random
# rand=random.randint(1,100)
# print(rand)
#
# guesses=0
# userGuess=None
#
# # guess=int(input('Enter your guess:'))
#
# while rand!=userGuess:
#     guess = int(input('Enter your guess:'))
#     guesses+=1
#     if guess>rand:
#         print('You\'re too high on numbers,come down')
#
#     elif guess<rand:
#         print('You\'re too low on numbers,go up')
#
#     elif guess==rand:
#         print('Wow,correct guess!')
#         break
#
#
#
# print(f'You guessed the number in {guesses} guesses')
#
#
# with open('Highscore.txt','r') as f:
#     hiscore=int(f.read())
#
# if guesses<hiscore:
#     print('You just broke the highscore')
#     with open('Highscore.txt','w') as g:
#         g.write(str(guesses))
#
