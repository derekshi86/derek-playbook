hungry = True
if hungry:
    print("go eat")
else:
    print("go play")

scores = 70
if scores == 100:
    print("best")
elif scores >=80:
    print("HD")
elif scores >=60:
    print("C")
elif scores >=40:
    print("P")
else:
    print("failed")


if scores == 100 and hungry:
    print("AAAAAAAA")
elif scores == 100 or hungry:
    print("CCCCCC")
elif scores == 100 or not(hungry):
    print("DDDDDD")
else:
    print("BBBBBBBB")

if scores != 100:
    print("It's not 100")
else:
    print("100")


def max_num(num1,num2,num3):
    data = [float(num1),float(num2),float(num3)]
    print(data)
    result = max(data)
    return result

compare = max_num(80.12, 99.33, 5555.001)
print(compare)
