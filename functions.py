FILEPATH = "todos.txt"
FILEPATH2 = "done_todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes todo items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def get_done_todos(filepath2=FILEPATH2):
    with open(filepath2, 'r') as file_local2:
        done_todos_local = file_local2.readlines()
    return done_todos_local


def write_done_todos(done_todos_arg, filepath2=FILEPATH2):
    """ Writes todo items list in the text file"""
    with open(filepath2, 'w') as file2:
        file2.writelines(done_todos_arg)


if __name__ == "__main__":
    print("hello from functions")
