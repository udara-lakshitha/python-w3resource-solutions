# 10. Number Expansion Calculator

def get_the_answer(n: str) -> int:
    '''
    This function will return n + nn + nnn
    '''
    first_term = int(n)
    second_term = int(n*2)
    third_term = int(n*3)
    return first_term + second_term + third_term

if __name__ == '__main__':
    n = input('Enter a value for n: ')
    print(f'{n} + {n*2} + {n*3} = {get_the_answer(n)}')