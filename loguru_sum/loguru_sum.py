from loguru import logger
import time

def sum(a, b):
    c = a + b
    print(c)
try:
 start = time.time()
 sum(1, 2)
 end = time.time()
 total = end - start
 logger.success(f"success, Виконано за {total} секунд")
except TypeError:
   logger.error("What?")