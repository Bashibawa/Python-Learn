from pickletools import markobject

from yaml import Mark


print ('Welcome to Askpython Quiz')
answer=input('Are you ready to play the Quiz? (yes/no):')
score=0
total_questions=3
if answer.lower()=='yes':
    answer=input('Question 1: What is your Favourite progamming language?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 2: Do you follow any author on Askpython?')
    if answer.lower()=='yes':
        score +=1
        print('correct')
    else:
        print('Wrong Answer :(')
    answer=input('Question 3: What is the name of your Favourite website for learning Python?')
    if answer.lower()=='askpython':
        score +=1
        print('correct')
    else:
        print('Wrong Answer :(')
else:
    ("You just exited AskPython Quiz game")

print('Thank you for playing this small quiz game, you attemted', score, "questions correctly!")
Mark = (score/total_questions)*100
print('Marks obtained: ', Mark)
print('BYE!')