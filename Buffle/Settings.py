# used to configure Buffle to a user's liking

# variables alterable by the users
display_results = True  # displays in terminal the result of a method


# displays in terminal if file was altered
def result(file: str, method: str, value, unaltered,):
    """
    :param file: target file's location / root
    :param method: name of the method / action done in method
    :param value: new value after alteration
    :param unaltered: value that causes no changes to file
    :return: displays in terminal the outcome of a method
    """
    if display_results:
        if value != unaltered:
            print(f"{file} <|> {method} <|> was altered [{value}]")
        else:
            print(f"{file} <|> {method} <|> was unaltered [{value}]")
