from loguru import logger
from functools import wraps
import time

# logger.add("file_{time}.log", format="{time} {level} {message}", level="INFO")

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # logger.info(f"Chamando a função '{func.__name__}' com argumentos {args} e {kwargs}")
        resultado = func(*args, **kwargs)
        # logger.info(f"A função '{func.__name__}' retornou {resultado}")
        return resultado     
    return wrapper

def cronometro(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        logger.info(f"A função {func.__name__} levou {fim - inicio:.4f} segundos.")
        return resultado
    return wrapper

# def hello(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print("Isso e um decorador")
#         return result
#     return wrapper

# @log_decorator
# @cronometro
# def funcao_2_seg():
#     """Esta função simula um processamento demorado."""
#     time.sleep(2)

# @log_decorator
# @cronometro
# def funcao_6_seg():
#     """Esta função simula um processamento ainda mais demora."""
#     time.sleep(6)
    

# funcao_2_seg()
# print(funcao_2_seg.__name__)  # Saída: funcao_demorada
# print(funcao_2_seg.__doc__)   # Saída: Esta função simula um processamento demorado.

# funcao_6_seg()
# print(funcao_6_seg.__name__)
# print(funcao_6_seg.__doc__)