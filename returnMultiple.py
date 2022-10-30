import random

def get_values():
    x = random.randint(0, 10)
    y = random.randint(0, 10)

    return [x, y]

x, y = get_values()

print(x, y)

