import random

numbers = range(1,46)
print(numbers)
print(list(numbers))

lotto = random.sample(numbers, 6)
lotto = random.sample(range(1, 46), 6)
print(lotto)