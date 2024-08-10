import random
 
#print 5 random numbers between 1 and 70 and 1 random number between 1 and 27

def powerball():
    numbers = []
    for i in range(5):
        numbers.append(random.randint(1, 70))
    numbers.append(random.randint(1, 27))
    return numbers 

print(powerball())

#print the numbers in descending order

numbers = powerball()
numbers.sort(reverse=True)
print(numbers)

