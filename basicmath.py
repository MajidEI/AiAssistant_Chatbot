from math import sqrt, cos, sin, tan, cosh, sinh, tanh, log, pi, log10

def calculate(expression):
    try:
        r = eval(expression)
        return (r)
    except:
        return ("expression invalid")
