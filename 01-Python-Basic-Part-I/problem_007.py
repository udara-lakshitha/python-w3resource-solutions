# 7. File Extension Extractor

import os

def get_extension(filename: str) -> str:
    '''
    This function returns the file extension.
    If there is no file extension, it will be provided an error message
    '''
    root, extension = os.path.splitext(filename)
    if extension:
        return extension[1:]
    return 'There is no file extension'

if __name__ == '__main__':
    file_name = input("Enter the file name with extension: ")
    function_response = get_extension(filename = file_name)
    print(function_response)