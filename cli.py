from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()
    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:] + '\n'
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}. {item.capitalize()}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            listnumber = int(user_action[5:])
            print ("You'll replace item # ", listnumber, " in your to do list")
            todos = get_todos()
            new_entry = input("Please enter the new to do to edit the list: ")
            todos[listnumber-1] = new_entry + '\n'
            write_todos(todos)
        except ValueError:
            print("Your command isn't valid. Please type edit and the number on the list you want to edit")
            continue

    elif user_action.startswith("complete"):
        try:
            listnumber = int(user_action[9:])
            todos = get_todos()
            todo_to_remove = todos[listnumber-1].strip('\n')
            todos.pop(listnumber-1)
            write_todos(todos)
            message = f"{todo_to_remove.capitalize()} was removed from the list"
            print(message)
            print ("Your new list is:")
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}. {item.capitalize()}"
                print(row)
        except IndexError:
            print("The number you entered is not on the list of todos")
            continue
        except ValueError:
            print("Your command isn't valid. Please type complete and the number on the list you want to mark as completed")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("The command you entered isn't valid, please enter a valid command")
print("Good bye!")
