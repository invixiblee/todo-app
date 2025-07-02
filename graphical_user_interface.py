
import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter to-do", key='to-do')
addb = sg.Button("Add")

window = sg.Window('My To-Do App', 
                   layout=[[label], [input_box, addb]], 
                   font=('Helvetica', 13))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.gtodos()
            ntodo = values['to-do'] + '\n'
            todos.append(ntodo)
            functions.wtodos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
