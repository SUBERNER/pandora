def make_list(variable):
    """
    makes sure a variable is always a list
    """
    if isinstance(variable, type(variable)):
        variable = [variable]
    return variable
