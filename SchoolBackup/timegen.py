import datetime
import random

randh = random.randint(1, 24)
randm = random.randint(0, 59)
ti = datetime.time(randh, randm, 0)
print(ti)
