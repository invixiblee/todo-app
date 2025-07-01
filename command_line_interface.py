#?

import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    action = input("Type add, show, edit, complete, or exit: ")
    action = action.strip()
    
    if action.startswith('add'):
        todo = action[4:]

        todos = functions.gtodos()

        todos.append(todo + '\n')

        functions.wtodos(todos)

    elif action.startswith('show'):
        todos = functions.gtodos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif action.startswith('edit'):
        try:
            num = int(action[5:])
            num = num - 1

            todos = functions.gtodos()

            ntodo = input("Enter new todo: ")
            todos[num] = ntodo + '\n'

            functions.wtodos(todos)

        except ValueError:
            print("Command is not valid")
            continue
        
        except IndexError:
            print("There is no item with that number")
            continue

    elif action.startswith('complete'):
        try:
            num = int(action[9:])

            todos = functions.gtodos()
            
            index = num - 1
            rtodo = todos[index].strip('\n')
            todos.pop(index)

            functions.wtodos(todos)
            
            print(f"Todo {num} ({rtodo}) was removed from the list")
        
        except ValueError:
            print("Command is not valid")
            continue
        
        except IndexError:
            print("There is no item with that number")
            continue

    elif action.startswith('exit'):
        break
    
    else:
        print("Command is not valid")

print("Bye!")
