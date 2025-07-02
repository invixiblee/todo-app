
import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter to-do", key='todo')
addb = sg.Button("Add")
listbox = sg.Listbox(values=functions.gtodos(), key='todos', 
                     enable_events=True, size=[45, 10])
editb = sg.Button("Edit")

window = sg.Window('My To-Do App', 
                   layout=[[label], [input_box, addb], [listbox, editb]], 
                   font=('Helvetica', 13))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])

    match event:
        case 'Add':
            todos = functions.gtodos()
            ntodo = values['todo'] + '\n'
            todos.append(ntodo)
            functions.wtodos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            todoe = values['todos'][0]
            ntodo = values['todo']

            todos = functions.gtodos()
            index = todos.index(todoe)
            todos[index] = ntodo + '\n'
            functions.wtodos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()
