secret_num = 77
guess = None
count = 0
limit = 3

while secret_num != guess and count <= limit:
    guess = float(input("guess input"))
    count = count +1
    if guess > secret_num and count < limit:
        print("guess a smaller number")
    elif guess < secret_num and count < limit :
        print("guess a larger number")
    elif guess == secret_num and count < limit:
        print("binggo")
    else:
        print("times up")
