#for letter in "hello":
#    print(letter)


#for num in range(0,99):
#    print(num)


#print(pow(2, 6))

def power(base_num,pow_num):
    result = base_num
    for index in range(pow_num-1):
        result = result * base_num
        print(index)
    return result

print(power(2,6))