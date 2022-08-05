scores = [90,70,60,50,80]
friends = ["A","B","C"]
scores[0] = 30

scores.extend(friends)
scores.append(400)
scores.remove(30)
scores.pop()
print(scores + friends)
print(scores[0:2])
print(scores[:4])
print(scores)
print(scores.index(60))
print(scores.count(99))
print(len(scores))
