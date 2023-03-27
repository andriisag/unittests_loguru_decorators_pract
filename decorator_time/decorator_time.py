from loguru import logger
def func_time(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        total = end - start
        logger.info(f"Виконано за {total} секунд")
        return res
    return wrapper
@func_time
def sum(a, b):
    print(a + b)
sum(1, 2)
