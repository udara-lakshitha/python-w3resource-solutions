# 5. Reverse Full Name

def reverse_name(full_name: str) -> str:
    '''
    This function will reverse the given full name.
    If the length is 0 or 1, return the exact same name which is provided.
    Otherwise, removing leading and traililng spaces and split into a list.
    After that, will return the reversed name as a string.
    '''
    if len(full_name) <= 1:
        return full_name
    name_parts = full_name.strip().split()
    return ' '.join(name_parts[::-1])

if __name__ == '__main__':
    full_name = input('Enter the full name: ')
    print(reverse_name(full_name = full_name))