
import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter to-do")
addb = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, addb]])
window.read()
window.close()
