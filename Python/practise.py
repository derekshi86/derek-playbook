from question import Question
test = [
    "1+3=?\n\n(a) 2\n(b) 3\n(c) 4\n\n",
    "1m=?cm\n\n(a) 10\n(b) 100\n(c) 1000\n\n",
    "what color is banana\n\n(a) red\n(b) black\n(c) yellow\n\n"
]

questions = [
    Question(test[0],"c"),
    Question(test[1],"b"),
    Question(test[2],"c")
    ]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.desciption)
        if answer == question.answer:
            score += 1
    
    print("your score is " + str(score) + " in total " + str(len(questions)) + " questions")


run_test(questions)