from typing import AnyStr

#Getting started
print('Hello to the game  :')
answer = input('wanna play some Quizz ? ' )
if answer.lower() != "yes":
    quit()
print("Okay lets get started :) ")
#The Quizz Questions
score = 0
answer = input('what is the capital of Morocco : ')
if answer.lower() == 'rabat':
    print('Correct ! ')
    score += 1 
else: 
    print('Incorrect')


answer = input('what is the capital of Spain : ')
if answer.lower() == 'madrid':
    print('Correct ! ')
    score += 1 
else: 
    print('Incorrect')
answer = input('what is the capital of France : ')
if answer.lower() == 'paris':
    print('Correct ! ')
    score += 1 
else: 
    print('Incorrect')
    answer = input('what is the capital of Algeria : ')
if answer.lower() == 'alger':
    print('Correct ! ')
    score += 1 
else: 
    print('Incorrect')    
    answer = input('what is the capital of Germany : ')
if answer.lower() == 'berlin':
    print('Correct ! ')
    score += 1 
else: 
    print('Incorrect')    
    answer = input('what is the capital of England : ')
if answer.lower() == 'london':
    print('Correct ! ')
    score += 1 
else: 
    print('Incorrect')    
    answer = input('what is the capital of south korea : ')
if answer.lower() == 'seol':
    print('Correct ! ')
    score += 1 
else: 
    print('Incorrect')    
answer = input('what is the capital of Australia : ')
if answer.lower() == 'canberra':
    print('Correct ! ')
    score += 1 
else: 
    print('Incorrect')    
    answer = input('what is the capital of Holland : ')
if answer.lower() == 'amsterdam':
    print('Correct ! ')
    score += 1 
else: 
    print('Incorrect')    
    answer = input('what is the capital of Egypt : ')
if answer.lower() == 'cairo':
    print('Correct ! ')
    score += 1 
else: 
    print('Incorrect')    
#Results
print('Congrats you ended the test ! ')
print('you got ',str(score),'Correct Answers of 10')
print((score*100)/10,'%')