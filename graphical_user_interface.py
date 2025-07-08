
import functions
import FreeSimpleGUI as sg
import time

sg.theme('Black')

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter to-do", key='todo')
addb = sg.Button("Add", size=10)
listbox = sg.Listbox(values=functions.gtodos(), key='todos', 
                     enable_events=True, size=[45, 10])
editb = sg.Button("Edit")
completeb = sg.Button("Complete")
exitb = sg.Button("Exit")

window = sg.Window('My To-Do App', 
                   layout=[[clock],
                           [label], 
                           [input_box, addb], 
                           [listbox, editb, completeb], 
                           [exitb]], 
                   font=('Helvetica', 13))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case 'Add':
            todos = functions.gtodos()
            ntodo = values['todo'] + '\n'
            todos.append(ntodo)
            functions.wtodos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            try:
                todoe = values['todos'][0]
                ntodo = values['todo']

                todos = functions.gtodos()
                index = todos.index(todoe)
                todos[index] = ntodo + '\n'
                functions.wtodos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 13))

        case 'Complete':
            try:
                todoc = values['todos'][0]
                todos = functions.gtodos()
                todos.remove(todoc)
                functions.wtodos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 13))

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()
