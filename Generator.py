from typing import Callable

text = "Загальний дохід працівника складається з декількох частин: "\
    "1000.01 як основний дохід, доповнений додатковими надходженнями"\
    " 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    import re
    pattern = r'\b\d+\.\d+\b'
    numbers = re.findall(pattern, text)
    return [float(num) for num in numbers]

def sum_profit(text: str, func: Callable[[str], list]):
    sum_profit = 0
    numbers = func(text)
    for i in numbers:
        sum_profit += i
    return sum_profit
    
result = sum_profit(text, generator_numbers)
print(f"Загальний дохід {result}")
