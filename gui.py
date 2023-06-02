import functions
import PySimpleGUI as sg
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="user_input")
add_button = sg.Button("Add")
window = sg.Window('To Do - List',
                   layout=[[label], [input_box, add_button]],
                   font=('Gill Sans', 15))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['user_input'] + "\n")
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
