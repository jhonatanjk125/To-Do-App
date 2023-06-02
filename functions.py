FILEPATH = "listoftodos.txt"

def get_todos(filepath=FILEPATH):
    """" Read the list of todos. """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local
def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the list of todos in the text file. """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)