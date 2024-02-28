#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    check = sys.argv[2]
    operator = {'+': add, '-': sub, '*': mul, '/': div}

    if check not in list(operator.keys()):
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    print('{} {} {} = {}' .format(a, check, b, operator[check](a, b)))
