from time import time


def log(filename="mylog.txt"):
    """Внешняя функция принимает элементы функции и возвращает декоратор"""

    def decorator(func):
        """Принимает функцию, возвращает обертку"""

        def wrapper(*args, **kwargs):
            """Функция-обертка"""
            if filename is None:

                try:

                    start_time = time()

                    result = func(*args, **kwargs)

                    end_time = time()

                    print(f"{func.__name__} ok, start func: {start_time}, end func: {end_time}")
                    return result
                except Exception as error:

                    print(f"{func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}")

            else:

                try:

                    start_time = time()

                    end_time = time()

                    with open(filename, "a") as file:

                        file.write(f"{func.__name__} ok, start func: {start_time}, end func: {end_time}")

                except Exception as error:

                    with open("filename", "a") as file:

                        file.write(f"{func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}")

        return wrapper

    return decorator
