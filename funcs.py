import math
from typing import Any
import numpy as np

def f(x) -> float | Any:
    """
    Сама функция, которая нуждается в интегрировании
    :param x:
    :return:
    """
    try:
        return math.exp(x**2)
    except:
        return np.nan
# метод прямоугольника
def rect(func, a, b, divisions) -> float | Any:
    """
    Метод прямоугольников
    :param func: Функция
    :param a: Нижняя граница
    :param b: Верхняя граница
    :param divisions: Разделения (чем больше - тем выше точность)
    :return: Численное значения интеграла
    """
    h = (b - a) / divisions
    result = 0
    # print(x)
    try:
        for i in range(divisions):
            x = a + i * h
            result += h * func(x)
        return result
    except:
        return np.nan
# формула трапеций
def trapezoidal(func, a, b, divisions) -> float | Any:
    """
    Формула трапеции
    :param func: Функция
    :param a: Нижняя граница
    :param b: Верхняя граница
    :param divisions: Разделения (чем больше - тем выше точность)
    :return: Численное значения интеграла
    """
    h = (b - a) / divisions
    H = h / 2
    try:
        result = H * (func(a) + func(b))
        if divisions > 2:
            for i in range(1, divisions-1):
                x = a + i * h
                result += H * 2 * func(x)
        return result
    except:
        return np.nan

# формула симпсона
def simpson(func, a, b, divisions) -> float | Any:
    """
    Формула Симпсона
    :param func: Функция
    :param a: Нижняя граница
    :param b: Верхняя граница
    :param divisions: Разделения (чем больше - тем выше точность)
    :return: Численное значения интеграла
    """
    h = (b - a) / divisions
    H = h / 3
    try:
        result = H * (func(a) + func(b))
        if divisions > 2:
            for i in range(1, divisions):
                x = a + i * h
                if i % 2 == 0:
                    result += H * 2 * func(x)
                if i % 2 != 0:
                    result += H * 4 * func(x)
        return result
    except:
        return np.nan
