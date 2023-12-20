from datetime import timedelta
from datetime import datetime
import platform
import os
import random
numbers = [i*i for i in range(5)]
# Inserta la línea de código aquí.
foo = list(filter(lambda x: x % 2, numbers))
print(foo)


a = random.randint(0, 100)
b = random.randrange(0, 100, 3)
c = random.choice((0, 100, 3))

print(a, b, c)

var = os.uname()
print(var)


system_info = platform.uname()


datetime_1 = datetime(2019, 11, 27, 11, 27, 22)
datetime_2 = datetime(2019, 11, 27, 0, 0, 0)

print(datetime_1 - datetime_2)


delta = timedelta(weeks=1, days=7, hours=11)
print(delta * 2)
