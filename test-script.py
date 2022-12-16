import random
import sys
import time

def typing(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()

        time.sleep(random.random() * 0.3)

typing('Hi , this is first my program')
