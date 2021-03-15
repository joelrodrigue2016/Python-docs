# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:01:20 2020

@author: 18134
"""
from Question import Question
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Red/Green\n(b) Purple\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Red/Green\n(b) Purple\n(c) blue\n\n",
    "Who is your favorite pet cat?\n(a) dino\n(b) fuego\n(c) Rambo\n\n",
]

questions = [
       Question(question_prompts[0], "a"),
       Question(question_prompts[1], "c"),
       Question(question_prompts[2], "b"),
       Question(question_prompts[3], "c"),
       
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/4" + " questions correct!")
    print("You are encoraged to try again")
    print("My name is Joel Rodriguez and I am here to help!")
    
    
run_test(questions)

