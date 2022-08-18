file = open("Python/123.txt", mode="a", encoding="utf-8")
#print(file.read())
#print(file.readline())
#print(file.readlines())
file.write("\nhello")
file.close()



with open("Python/123.txt", mode="a", encoding="utf-8") as file:
    file.write("\nxxxxxxxx")