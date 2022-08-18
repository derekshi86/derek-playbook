secret_num = 77
guess_num = None
guess_limit = 3
guess_count = 0
out_of_limit = False

while secret_num != guess_num and not(out_of_limit):
    guess_count += 1
    if guess_count <= guess_limit:
        guess_num = int(input("please enter your guess: "))
        if guess_num > secret_num:
            print("enter a smaller number")
        elif guess_num < secret_num:
            print("enter a larger number")
    else: out_of_limit = True

if out_of_limit:
    print("times up")
else:
    print("bingo")