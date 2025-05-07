def read_file(file_path: str) -> str:
    """
    Reads the contents of a file and returns it as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_file(file_path: str, content: str) -> None:
    """
    Writes the given content to a file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def list_files_in_directory(directory_path: str) -> list:
    """
    Returns a list of files in the specified directory.
    """
    return [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]

#     import os

#     return os.listdir(directory_path)


def generate_numbers(n: int) -> iter:
    """
    Generates a sequence of numbers from 0 to n-1 using an iterator.
    """
    return iter(range(n))


def use_function_from_module(module_name: str, function_name: str, *args) -> any:
    """
    Demonstrates how to import a function from another script (module) and execute it.
    The module name and function name are passed as strings, along with any arguments for the function.
    """
    import importli
    module = importlib.import_module(module_name)
    func = getattr(module, function_name)
    return func(*args)