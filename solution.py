import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 478097435 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    x = x**2
    sn = sum(x)
    return (sn/(29*chi2.ppf((1 - alpha / 2), df=2*len(x))))**0.5, \
           (sn/(29*chi2.ppf(alpha / 2,df=2*len(x))))**0.5
