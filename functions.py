FILEPATH = "todos.txt"
FILEPATH2 = "done_todos.txt"
def get_todos(filepath=FILEPATH):
    """ Reads the text file and returns the
    list of todo items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes todo items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def get_done_todos(filepath=FILEPATH2):
    """ Reads the text file and returns the
    list of todo items"""
    with open(filepath, 'r') as file_local:
        done_todos_local = file_local.readlines()
    return done_todos_local


def write_done_todos(done_todos_arg, filepath=FILEPATH2):
    """ Writes todo items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(done_todos_arg)


if __name__ == "__main__":
    print("hello from functions")