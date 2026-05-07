import functools


def log(filename=None):
    """
       Декоратор, который  логирует  начало и конец выполнения функции, ее результаты или возникшие ошибки.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
                raise

        return wrapper

    return decorator


# Пример функции с использованием декоратора
@log(filename="mylog.txt")
def divide_function(x, y):
    return x / y


divide_function(4, 2)
