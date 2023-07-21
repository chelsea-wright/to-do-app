from functions import get_todos, write_todos
import time
print(time.strftime("%b %d, %Y, %H:%M:%S"))
while True:
    user_input = input("Input either add, show, edit, complete, or exit: ")
    user_input = user_input.strip().casefold()

    if user_input.startswith('add'):
        user_input = user_input[4:]
        object_list = get_todos()
        object_list.append(user_input + '\n')

        write_todos(object_list)


        print(user_input.capitalize().strip() + " Was added to the list")
        # item = f"{item_to_add}:it's this"
    elif user_input.startswith('show'):

        object_list = get_todos()

        new_todos = [item.strip('\n') for item in object_list]
        for index, item in enumerate(new_todos):
            row = f"{index + 1}.{item}"
            print(row)
    elif user_input.startswith('exit'):
        print("Goodbye")
        break
    elif user_input.startswith('edit'):
        try:
            user_input_num = int(user_input[5:])
            # print("TEST " + str(user_input_num))
            object_list = get_todos()
            for index, value in enumerate(object_list):
                print(f"{index + 1}.{value.strip()}")
            # user_input_num = int(input("Please enter the object number you'd like to edit: "))s
            input_from_user = input("Please enter the new value: ")

            object_list[user_input_num - 1] = input_from_user + "\n"
            write_todos(object_list)

        except ValueError:
            print("Please enter a # value after 'edit'")
            continue
        except IndexError:
            print("your list is empty!")

    elif user_input.startswith('complete'):
        try:
            user_input_num = int(user_input[8:])
            object_list = get_todos()
            for index, value in enumerate(object_list):
                print(f"{index + 1}.{value.strip()}")
            # user_input_num = int(input("Please enter the number of the task you've completed: "))

            object_list.pop(user_input_num - 1)
            write_todos(object_list)

        except IndexError:
            print("You've entered an input that is out of bounds. Please try again")
            continue
        except ValueError:
            print("Please enter a number to complete")
            continue
