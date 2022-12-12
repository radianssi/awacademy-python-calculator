
def sum_numbers(a, b):
    try:
        answer = a + b
        return answer
    except TypeError:
        return TypeError

def subtract_numbers(a, b):
    return (a - b)

def multiply_numbers(a, b):
    return float(a * b)

def divide_numbers(a, b):
    if b == 0:
        try:
            return float(a / b)
        except ZeroDivisionError:
            return ZeroDivisionError
    else:
        try:
            answer = float(a / b)
            return answer
        except TypeError:
            return TypeError