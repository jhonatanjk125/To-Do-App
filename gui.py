import functions
import PySimpleGUI as sg
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="user_input")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos-list', enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window('To Do - List',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
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
            window['todos-list'].update(values=todos)
        case "Edit":
            todo_to_edit=values['todos-list'][0]
            new_todo = values['user_input'] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos-list'].update(values=todos)
        case 'todos-list':
            window['user_input'].update(value=values['todos-list'][0])
        case   sg.WIN_CLOSED:
            break

window.close()
