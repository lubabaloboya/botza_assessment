
from Question import Question

questions_prompts = [
    "What is the color of the sky?\n(a) Blue\n(b) Red\n(c) Green\n\n",
    "Who is the president of SA?\n(1) Thabo Mbeki\n(2) Jacob Zuma\n(3) Ramaphosa\n\n",
    "South Africa is a company ?\n(yes) 1\n(no) 20\n\n"
]

questions = [
    Question(questions_prompts[0], "a"),
    Question(questions_prompts[1], "3"),
    Question(questions_prompts[2], "no")
]

def run(questions):
    score = 0
    for question in questions:
        answer = input(questions_prompts)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")

run(questions)