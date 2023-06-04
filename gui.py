import functions
import PySimpleGUI as sg
import time
sg.theme("LightGreen2")
clock_label = sg.Text(time.strftime("%b %d, %Y %H:%M:%S"),key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="user_input")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos-list", enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


window = sg.Window('To Do - List',
                   layout=[[clock_label],
                           [label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Gill Sans', 14))
while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['user_input'] + "\n")
            functions.write_todos(todos)
            window['todos-list'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit=values['todos-list'][0]
                new_todo = values['user_input'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos-list'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=('Gill Sans', 14))
        case "Complete":
            try:
                todo_to_complete=values['todos-list'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos-list'].update(values=todos)
                window['user_input'].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=('Gill Sans', 14))
        case 'todos-list':
            window['user_input'].update(value=values['todos-list'][0])
        case "Exit":
            break
        case   sg.WIN_CLOSED:
            break

window.close()
