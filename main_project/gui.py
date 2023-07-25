import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="enter to-do")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box,add_button]],
                   font=("Helvetica", 20))
# displays the window on the screen
while True:
    event, values = window.read()
    print(event,values)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values[0] + "\n")
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()
