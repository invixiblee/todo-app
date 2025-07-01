#?

FILEPATH = 'todos.txt'

def gtodos(filepath=FILEPATH):
    with open(filepath, 'r') as lfile:
        ltodos = lfile.readlines()
    return ltodos

def wtodos(todosarg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todosarg)

if __name__ == "__main__":
    print("hello world")
