import random

bag= (f"‌")

bag_1= (random.choice(bag))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,0 ]

start_number = str(random.randint(0, 9))

result = start_number + '.' + '.'.join([str(random.choice(numbers)) for _ in range(10000000)])


print(f"\033[31m{bag_1}.\033[32m{result}")