# 6. List and Tuple Generator

def generate_list_and_tuple(numbers_str: str) -> tuple[list, tuple]:
    '''
    This function will return a list and a tuple for given numbers
    '''
    new_list = [number.strip() for number in numbers_str.split(',')]
    new_tuple = tuple(new_list)
    return new_list, new_tuple

if __name__ == '__main__':
    numbers = input('Enter all comma separated numbers: ')
    numbers_list, numbers_tuple = generate_list_and_tuple(numbers_str = numbers)
    print(f'List: {numbers_list}')
    print(f'Tuple: {numbers_tuple}')